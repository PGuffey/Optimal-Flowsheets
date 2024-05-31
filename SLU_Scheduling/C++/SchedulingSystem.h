#ifndef SCHEDULINGSYSTEM_H
#define SCHEDULINGSYSTEM_H

#include <string>
#include <vector>

using namespace std;

class Class {
public:
    string name;
    int creditHours;
    vector<string> prerequisites;
    bool concurrentEnrollment;

    Class(string name, int creditHours, vector<string> prerequisites, bool concurrentEnrollment);
};

class Block {
public:
    vector<Class> classes;
    int totalCredits;
    int maxCredits;
    Block* nextBlock;

    Block(int maxCredits = 18);

    bool insertClass(const Class& classToInsert);
    bool checkPrerequisites(const Class& classToInsert) const;
    void deleteClass(const Class& classToDelete);
    void tryToFill();
    void printBlock(int semesterNumber) const;  
};

#endif // SCHEDULINGSYSTEM_H
