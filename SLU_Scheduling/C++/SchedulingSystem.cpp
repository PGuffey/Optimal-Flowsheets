#include "SchedulingSystem.h"
#include <algorithm>
#include <iostream>

// Class constructor
Class::Class(string name, int creditHours, vector<string> prerequisites, bool concurrentEnrollment)
    : name(name), creditHours(creditHours), prerequisites(prerequisites), concurrentEnrollment(concurrentEnrollment) {}

// Block constructor
Block::Block(int maxCredits) : totalCredits(0), maxCredits(maxCredits), nextBlock(nullptr) {}

// Function to insert a class into the current block
bool Block::insertClass(const Class& classToInsert) {
    if (totalCredits + classToInsert.creditHours <= maxCredits) {
        classes.push_back(classToInsert);
        totalCredits += classToInsert.creditHours;
        return true;
    }
    return false;
}

// Function to check prerequisites
bool Block::checkPrerequisites(const Class& classToInsert) const {
    for (const auto& prereq : classToInsert.prerequisites) {
        bool found = false;
        for (const auto& cls : classes) {
            if (cls.name == prereq) {
                found = true;
                break;
            }
        }
        if (!found) {
            return false;
        }
    }
    return true;
}

// Function to delete a class from the current block
void Block::deleteClass(const Class& classToDelete) {
    auto it = remove_if(classes.begin(), classes.end(),
        [&classToDelete](const Class& cls) { return cls.name == classToDelete.name; });
    if (it != classes.end()) {
        totalCredits -= it->creditHours;
        classes.erase(it, classes.end());
    }
    if (nextBlock != nullptr) {
        tryToFill();
    }
}

// Function to try and fill the current block from the next block
void Block::tryToFill() {
    if (nextBlock != nullptr && !nextBlock->classes.empty()) {
        Class nextClass = nextBlock->classes.front();
        if (insertClass(nextClass)) {
            nextBlock->deleteClass(nextClass);
        }
    }
}

// Function to print the courses in the block
void Block::printBlock(int semesterNumber) const {
    cout << "Semester " << semesterNumber << ":\n";
    for (const auto& cls : classes) {
        cout << "  " << cls.name << " (" << cls.creditHours << " credits)\n";
    }
    cout << "Total Credits: " << totalCredits << "\n\n";
}
