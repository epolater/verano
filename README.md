# **VERANO**
#### Video Demo:  https://youtu.be/2kMSoaRfb-4

#### **Description**:

Verano is a scheduling application designed for project managers and executives to keep track of their projects. The main users of this website would be corporate construction companies that have multiple construction projects.

Widely used applications for scheduling and planning purposes are Oracle's Primavera and Microsoft's MS Project, both of which have online versions on the web. Verano is a simplified version, mostly inspired by Primavera. It can be used as an alternative light version for small-sized projects that can be planned with 50 to 100 activities at the current development stage. With improved versions, it can be used for more complex projects too.

#### **Distinctiveness and Complexity**:
As mentioned above, there are not many online scheduling applications available, and only a few big companies use the online versions of their main standalone desktop applications. Verano could be a simpler alternative to these applications.

Verano's Gantt chart is developed using pure JavaScript codes from scratch. Developing Gantt bars, time scale headers and bottom menus, and managing the state of JavaScript components was challenging, and had to satisfy the complexity requirement of this course. Apart from front-end complexity, the application logic itself is challenging to program. There are 10 views in Django, excluding standard login, logout, and register views for the back-end. On the front-end side, there are more than 20 functions to create a Gantt chart, edit items, and control views.


#### **Programs used to develop the Verano**:

- Python 3.1 with Django framework: To handle the back-end process such as database usage, rendering some part of pages, login, and registering
- SQLite3 : To communicate with database
- Bootsrap v5.2 : CSS framework for some part of page designs
- JavaScript  : Pure JavaScript with no library.

#### **How To Use**:

To see a demonstration of the application, use "erkan" as user name and "1234" for the  password.

* **Side Menu :** Side Menu is used to control the application. It can be used with button descriptions visible or hidden by switching the view from the top menu button. The Side Menu's control buttons are:
    - New Project : This button opens a new project creation window.
    - Open Project : Opens the selected project from the projects table.
    - Delete project : Deletes selected project(s) from the projects table.
    - Add activity :  Adds a new activity to the opened project.
    - Delete Activity : Deletes the selected activity from the activities table.
    - Run Schedule : Runs the schedule and calculates all dates and floats
    -
* **Bottom Menu :** Bottom menu shows project and activity details. It is possible to edit project and activity details on bottom menu. Bottom menu is visible by default, it can be hidden by pressing hide button on top-right side corner of the menu. Currently there is one tab for Projects section and two tabs for Activities Section. Each tab shows different details of each section. 

For Projects Section; on Generals Tab it is possible to edit project id and name. other details are default and no need to edit or change.

For Activities Section;
    - On Generals Tab it is possible to edit Activity di , name and durations.
    - Relationships tab is where you can make assignments to activities. It shows activities predecessors and successors on two different windows

* **Projects Section :** On projects section you can see all created projects with some basic project information such as start and finish dates of projects, duration and number of activities of each project.

* **Activities Section :** This section shows activities table and gannt chart side by side. Its possible to change gannt and activity table sizes by moving vertical seperation line.

* **Creating a project and activities :** 
    - After logging in to create a new project, click "New Project" button to see project creation window. After defining project id, name and start date click "Create" button.
    - Selecet checkbox for the created project and click "Open Project" button from side menu to open project
    - After opening projects "Activities" Section will be visible. Every project is created with first activity with default activity values. activity default duration is 5 days and default start date is project start date.
    - Click "Add Activity" button on side menu to add new activities.
    - Use bottom menu's "General Tab" to edit acitivities' name, id and duration values.
    - To determine activity start and finish dates, each ctivity must have a predecessor and successor activity (except start and finish activities). It is advised to assign at least one predecessor and one sucessor to every activity in order to have more accurate scheduling dates.
    - After completing activity predecessor and successor assignments press "Run schedule" button to see start and finish dates of activities. Run schedule calculates, start, finish, lates start, late finish and total float and free float of each activity.
    - On gannt section you can see gannt bars for each activity with activity description, start and finish dates.
    - Critical activities (which has 0 or less total float) are indicated as red bars on gantt section

#### **Improvement on application**:
Main improvement to be made on application can be summarized as below;
- Schedule Update : Update activity progress and calculate schedule based on redefined remaining durations after seleceted uodate cutoff date
- Resource Asignments: Assign manpower and materila resources to eah activity to see timely distribution of resources during project
- Baseline schedule: To save initial schedules as baseline and assign this baseline to updated schedule to compare planned and realized status of activities
- Gannt Chart editi options : Settings menu for gantt chart section to edit gantt bar shape (color, thickness etc), timescale zoom options, other basic optinos such as vertical and horizontal line visibility, critical path visibility etc.
- WBS structure : To create a work break down and assign each activity. Show it on activity table as headers. Grouping activities as per WBS structure.
- Layout settings : To edit layout such as column width, font style, font color on activity table and save it as layout view for each user's preferences. Column selection for visibilty.
- Calendar option for scheduling: Defining and assigning different calendar for each activity