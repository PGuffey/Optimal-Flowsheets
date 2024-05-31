#include "SchedulingSystem.h"
#include "CSVReader.h"

int main() {
    // Read courses from the CSV file
    string filePath = "C:\\Users\\guffe\\Desktop\\Computer_Science\\Projects\\Optimal-Flowsheets\\Projects\\CSV_iterations\\formatted_courses.csv"; // Update with your file path
    vector<Class> courses = readCoursesFromCSV(filePath);

    cout << "Courses read successfully. Total courses: " << courses.size() << endl;

    // Create the blocks
    Block firstSemester;
    Block secondSemester;
    Block thirdSemester;

    // Check if there are enough courses for the example
    if (courses.size() < 4) {
        cerr << "Error: Not enough courses in the CSV file for the example." << endl;
        return 3;
    }

    // Insert some courses into the first semester as an example
    firstSemester.insertClass(courses[882]);
    firstSemester.insertClass(courses[890]);
    firstSemester.insertClass(courses[894]);
    firstSemester.insertClass(courses[902]);
    firstSemester.insertClass(courses[903]);
    firstSemester.insertClass(courses[904]);
    firstSemester.insertClass(courses[905]);
    firstSemester.insertClass(courses[906]);
    firstSemester.insertClass(courses[907]);

    // Link the semesters
    firstSemester.nextBlock = &secondSemester;
    secondSemester.nextBlock = &thirdSemester;

    // Print the schedule
    cout << "Created Schedule:" << endl;
    firstSemester.printBlock(1);
    secondSemester.printBlock(2);
    thirdSemester.printBlock(3);

    return 0;
}
