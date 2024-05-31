# Optimal Scheduling System

## Project Overview

The Optimal Scheduling System aims to create an advanced scheduling tool that optimizes course schedules for students based on various criteria such as course prerequisites, credit hour limits, and concurrent enrollment rules. The ultimate goal is to help students plan their semesters as efficiently as possible, ensuring they meet all their academic requirements while minimizing the time they are in school. It will also allow students to see if adding classes, minors, or majors is possible and what a schedule with any addition would look like.

## Project Goals

- **Optimize Course Scheduling:** Develop algorithms to optimize course schedules based on student preferences and academic requirements.
- **Custom Data Structure:** Implement a unique data structure to handle course scheduling efficiently.
- **User-Friendly Interface:** Provide an intuitive interface for students to input their preferences and view their optimized schedules.

## Iteration v0.0.0

In the first iteration of the Optimal Scheduling System, we focused on building the foundation for the project. This included:

1. **Basic Scheduling Functionality:**
   - Read course data from a CSV file.
   - Insert courses into semester blocks.
   - Print the schedule to the console.

2. **Custom Data Structure:**
   - Defined a `Class` structure to represent individual courses.
   - Implemented a `Block` structure to represent semesters and manage course insertion, deletion, and prerequisites checking.

### Limitations of the Initial Iteration

While the first iteration provided a good starting point, it lacked an optimizing component. The current implementation inserts courses sequentially without considering optimization criteria such as:

- Balancing the workload across semesters.
- Ensuring prerequisites are met in the most efficient manner.
- Minimizing schedule conflicts.

Additionally, this iteration is designed for students who know exactly what classes they need to take. It is not designed for those who only know their major and need to figure out their courses. We recognize this flaw and aim to address it in future iterations.

## Future Improvements

Building on the foundation laid in the initial iteration, future improvements will focus on:

1. **Optimization Algorithms:**
   - Implementing algorithms to optimize course scheduling based on various criteria.
   - Developing a priority queue to handle course dependencies and prioritize course insertion.

2. **Enhanced Data Structure:**
   - Expanding the custom data structure to support more complex scheduling requirements.
   - Integrating with a database to manage course data more effectively.

3. **User Interface:**
   - Creating a user-friendly interface for students to input their preferences.
   - Visualizing the optimized schedule in an intuitive manner.

## How to Run the Project

### Prerequisites

- Visual Studio 2022
- C++ compiler
- CSV file with course data (`formatted_courses.csv`)

### Steps to Run

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/OptimalSchedulingSystem.git
   cd OptimalSchedulingSystem
   ```

2. **Open the Project in Visual Studio 2022:**

   - Open Visual Studio 2022.
   - Go to `File > Open > Project/Solution`.
   - Select the `Optimal_Schedules_v0.0.0.sln` file.

3. **Build the Project:**

   - Go to `Build > Build Solution` or press `Ctrl+Shift+B`.

4. **Run the Project:**

   - Press `F5` to run the project.

### Sample CSV File

Create a sample CSV file named `test_courses.csv` with the following content to test the system:

```csv
prerequisites,name,creditHours,concurrentEnrollment
,CSCI 1010: Introduction to Computer Science,3,FALSE
,CSCI 1020: Advanced Computer Science,4,FALSE
,NEUR 1010: Introduction to Neuroscience,3,FALSE
CSCI 1010,CSCI 2010: Data Structures,4,FALSE
NEUR 1010,NEUR 2010: Advanced Neuroscience,3,FALSE
```

### Acknowledgements

This project is an ongoing effort to improve course scheduling for students. We acknowledge that the first iteration is a starting point and appreciate any feedback or contributions to enhance the system further.

## Contributions

We welcome contributions to the project. If you have suggestions or improvements, please feel free to submit a pull request or open an issue on GitHub.

---

Thank you for your interest in the Optimal Scheduling System. Together, we can create a tool that significantly improves the academic planning experience for students.
