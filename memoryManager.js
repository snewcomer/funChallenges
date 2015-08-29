function Block(start, size) {
  this.start = start;
  this.size = size;
}


/**
 * @constructor Creates a new memory manager for the provided array.
 * @param {memory} An array to use as the backing memory.
 */
function MemoryManager(memory){
  this.memory = memory;
  this.blocks = [];
}

/**
 * Allocates a block of memory of requested size.
 * @param {number} size - The size of the block to allocate.
 * @returns {number} A pointer which is the index of the first location in the allocated block.
 * @throws If it is not possible to allocate a block of the requested size.
 */
MemoryManager.prototype.allocate = function(size) {
  var i, pointer = 0;
  for (i = 0; i < this.blocks.length; i++) {
    if (this.blocks[i].start - pointer >= size) {
      this.blocks.splice(i, 0, new Block(pointer, size));
      return pointer;
    }
    pointer = this.blocks[i].start + this.blocks[i].size;
  }
  if (this.memory.length - pointer >= size) {
    this.blocks.push(new Block(pointer, size));
    return pointer;
  }
  
  throw "Not possible to allocate a new block of size " + size + ".";
};

/**
 * Releases a previously allocated block of memory.
 * @param {number} pointer - The pointer to the block to release.
 * @throws If the pointer does not point to an allocated block.
 */
MemoryManager.prototype.release = function(pointer){
  var i;
  for (i = 0; i < this.blocks.length; i++) {
    if (this.blocks[i].start == pointer) {
      this.blocks.splice(i, 1);
      return;
    }
  }
  
  throw "Pointer was not to an allocated block.";
};

/**
 * Reads the value at the location identified by pointer
 * @param {number} pointer - The location to read.
 * @returns {number} The value at that location.
 * @throws If pointer is in unallocated memory.
 */
MemoryManager.prototype.read = function(pointer){
  var i;
  for (i = 0; i < this.blocks.length; i++) {
    if (pointer >= this.blocks[i].start && pointer < this.blocks[i].start + this.blocks[i].size) {
      return this.memory[pointer];
    }
  }
  
  throw "Address was not in an allocated block."
}

/**
 * Writes a value to the location identified by pointer
 * @param {number} pointer - The location to write to.
 * @param {number} value - The value to write.
 * @throws If pointer is in unallocated memory.
 */
MemoryManager.prototype.write = function(pointer, value) {
  var i;
  for (i = 0; i < this.blocks.length; i++) {
    if (pointer >= this.blocks[i].start && pointer < this.blocks[i].start + this.blocks[i].size) {
      this.memory[pointer] = value;
      return;
    }
  }
  
  throw "Address was not in an allocated block."
}
