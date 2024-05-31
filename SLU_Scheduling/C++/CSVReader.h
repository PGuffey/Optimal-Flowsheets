#ifndef CSVREADER_H
#define CSVREADER_H

#include "SchedulingSystem.h"
#include <fstream>
#include <sstream>
#include <iostream>

using namespace std;

vector<Class> readCoursesFromCSV(const string& filePath) {
    vector<Class> courses;
    ifstream file(filePath);

    if (!file.is_open()) {
        cerr << "Error: Could not open file " << filePath << endl;
        exit(3);
    }

    string line;
    // Skip the header
    getline(file, line);

    while (getline(file, line)) {
        stringstream ss(line);
        string token;
        vector<string> tokens;

        while (getline(ss, token, ',')) {
            tokens.push_back(token);
        }

        if (tokens.size() < 4) {
            cerr << "Error: Incomplete line in CSV: " << line << endl;
            continue; // Skip incomplete lines
        }

        string prerequisitesStr = tokens[0];
        vector<string> prerequisites;
        if (!prerequisitesStr.empty()) {
            stringstream prereqStream(prerequisitesStr);
            string prereq;
            while (getline(prereqStream, prereq, ';')) {
                prerequisites.push_back(prereq);
            }
        }

        string name = tokens[1];
        int creditHours = stoi(tokens[2]);
        bool concurrentEnrollment = (tokens[3] == "TRUE");

        courses.emplace_back(name, creditHours, prerequisites, concurrentEnrollment);
    }

    if (courses.empty()) {
        cerr << "Error: No courses found in the CSV file." << endl;
        exit(3);
    }

    return courses;
}

#endif // CSVREADER_H
