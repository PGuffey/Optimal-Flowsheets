# College Class Scheduling System

## Goal
The goal of this system is to efficiently manage college class schedules. The system allows for inserting and deleting classes based on various constraints like credit hours, prerequisites, and concurrent enrollment. The data structure used is a linked list where each node represents a semester block containing courses.

## Data Structures

### Class
Represents individual college classes.
- **Attributes**:
  - `name`: (string) The name of the class.
  - `creditHours`: (int) Number of credit hours for the class.
  - `prerequisites`: (list of string) List of prerequisite class names.
  - `concurrentEnrollment`: (boolean) Indicates if concurrent enrollment is allowed with prerequisites.

### Block
Represents a semester, containing classes and managing the total credit hours.
- **Attributes**:
  - `classes`: (list of Class) A list of classes in the block.
  - `totalCredits`: (int) Total credit hours in the block.
  - `maxCredits`: (int, default 18) Maximum allowable credit hours in the block.
  - `nextBlock`: (Block) Link to the next semester block.

## Functions

### insertClass
Inserts a class into the current block if conditions are met, or moves to the next block.
- **Parameters**:
  - `currentBlock`: (Block) The current block where insertion is attempted.
  - `classToInsert`: (Class) The class to be inserted.
- **Returns**: (boolean) True if insertion is successful, False otherwise.

### checkPrerequisites
Checks if all prerequisites of a class are met within the current and previous blocks.
- **Parameters**:
  - `currentBlock`: (Block) The current block being checked.
  - `classToInsert`: (Class) The class whose prerequisites are being checked.
- **Returns**: (boolean) True if all prerequisites are met, False otherwise.

### deleteClass
Removes a class from a block and adjusts the total credit hours.
- **Parameters**:
  - `currentBlock`: (Block) The block from which the class is to be deleted.
  - `classToDelete`: (Class) The class to be removed.

### tryToFill
Attempts to fill the current block with classes from the next block after a deletion.
- **Parameters**:
  - `currentBlock`: (Block) The current block to be filled.
- **Returns**: (boolean) True if successful in filling the block, False otherwise.

## Implementation Notes
- Each function needs to handle edge cases like blocks being full or classes having no prerequisites.
- The system should be robust enough to manage multiple blocks linked together, each representing a semester.



----------------------------------------------------------------------------------------------------------------
# Pseudocode: 

## class Class:
-     name: string
-     creditHours: int
-     prerequisites: list of string
-     concurrentEnrollment: boolean

## class Block:
-     classes: list of Class
-     totalCredits: int
-     maxCredits: int = 18
-     nextBlock: Block


### Insertion:
function insertClass(currentBlock, classToInsert):
    if currentBlock.totalCredits + classToInsert.creditHours <= currentBlock.maxCredits:
        if checkPrerequisites(currentBlock, classToInsert):
            currentBlock.classes.append(classToInsert)
            currentBlock.totalCredits += classToInsert.creditHours
        else:
            // Handle prerequisites not met
            return False
    else:
        if currentBlock.nextBlock is null:
            currentBlock.nextBlock = new Block()
        return insertClass(currentBlock.nextBlock, classToInsert)

### Checking Prrequisites:
function checkPrerequisites(currentBlock, classToInsert):
    for prerequisite in classToInsert.prerequisites:
        found = False
        tempBlock = currentBlock
        while tempBlock is not null and not found:
            for class in tempBlock.classes:
                if class.name == prerequisite:
                    if not classToInsert.concurrentEnrollment:
                        if tempBlock == currentBlock:
                            return False
                    found = True
                    break
            tempBlock = tempBlock.nextBlock
        if not found:
            return False
    return True


### Deletion:
function deleteClass(currentBlock, classToDelete):
    currentBlock.classes.remove(classToDelete)
    currentBlock.totalCredits -= classToDelete.creditHours
    if currentBlock.nextBlock is not null:
        tryToFill(currentBlock)

### Optimizing // Refilling block:
function tryToFill(currentBlock):
    nextClass = currentBlock.nextBlock.classes[0]  // Assuming non-empty next block
    if insertClass(currentBlock, nextClass):
        deleteClass(currentBlock.nextBlock, nextClass)
    else:
        // Handling when the class cannot be moved to the current block
        return False


## Optimization Idea:

### Optimizer:
function optimizeSchedule(startBlock):
    currentBlock = startBlock
    while currentBlock is not null:
        if currentBlock.totalCredits < optimalCreditsPerSemester:
            if currentBlock.nextBlock is not null:
                attemptToPullClasses(currentBlock)
        elif currentBlock.totalCredits > optimalCreditsPerSemester:
            attemptToPushClasses(currentBlock)
        currentBlock = currentBlock.nextBlock

### Pull (similar to Refill):
function attemptToPullClasses(currentBlock):
    nextBlock = currentBlock.nextBlock
    for class in nextBlock.classes:
        if canMoveClassToCurrentBlock(currentBlock, class) and checkPrerequisites(currentBlock, class):
            moveClass(currentBlock, nextBlock, class)
            if currentBlock.totalCredits >= optimalCreditsPerSemester:
                break

### Push (customized insert):
function attemptToPushClasses(currentBlock):
    nextBlock = currentBlock.nextBlock or new Block()
    for class in currentBlock.classes:
        if canMoveClassToNextBlock(nextBlock, class) and checkPrerequisites(nextBlock, class):
            moveClass(nextBlock, currentBlock, class)
            if currentBlock.totalCredits <= optimalCreditsPerSemester:
                break
