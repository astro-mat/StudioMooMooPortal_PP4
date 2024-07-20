# Studio Moo Moo Client PortaL

![AmIResponsive image of Studio Moo Moo Client Portal](doc/amiresponsive.webp)

## Introduction

This project is to build a front-end client portal for an existing recording studio website (www.studiomoomoo.ie) where you, as a user can book a recording session and access other features.

## Table of Contents
<!--- TO BE GENERATED -->

## User Experience

### User Goals

One of the user goals is to be able to book . They should have a smooth user experience with the 

The main user goal would be to be able to book sessions in the studio. Additionally, the user should have a seamless experience with full CRUD (Create, Read, Update, and Delete) functionality for managing their bookings. Further aims include allowing the user to listen to and download their projects that have been recorded in the studio such as rough mixes and stems and to view details about past bookings.

### Site Owner Goals

The site owner goal is to reduce communication needed when clients need to make bookings and access their data. It also aims to project a professional image and added value to the clients. A serrvice that would not normally be provided by competing studios

### User Stories

Six Epics were decided upon with a total of 39 user stories. All user stories can be viewed here [Projects board](https://github.com/users/astro-mat/projects/2/views/1). Each user story was categorized into one of the following classes: Must have, Should have, Could have, or Won't have. Points were given to each user story based on the estimated time required for completion.

| Class | Points | Percentage of total points |
| -------------- | --------- | --------------- |
| Must have | 62 p | 56 % |
| Should have | 16 p | 15 % |
| Could have | 8 p | 7 % |
| Won't have | 24 p | 22 % |

The following user stories were completed in the first release of Studio Moo Moo Client Portal. To view the Won't have, they are listed here [Projects board](https://github.com/users/astro-mat/projects/2/views/1).

#### Epic 1 - Initial project setup

**User Story - Django installation and configuration**

As a developer, I can install Django and support libraries so that I have the appropriate environment ready to be able to proceed with the development

- Acceptance Criteria 1  
When the project is opened in the browser the web page shows that there has been a successful installation.

**User Story - Hosting setup and configuration**

As a developer, I can create a hosting environment so that I can present the site to the end user

- Acceptance Criteria 1  
When the project app is opened on Heroku, the browser the web page shows that there has been a successful installation. 

#### Epic 2 - User Account Creation

**User Story - Access the registration page**

As a new user, I can easily find the registration page so that I can create an account

- Acceptance Criteria 1  
When I enter the client portal of the website and I am not logged in I should see a register button

- Acceptance Criteria 2  
When I click the Register button I should be brought to a registration form

**User Story - Complete the registration form**

As a new user, I can enter my personal details so that I can register a new account.

- Acceptance Criteria 1  
The  registration form includes fields for necessary information such as email, password etc.
- Acceptance Criteria 2  
The registration form has input validation.
- Acceptance Criteria 3  
Once the user has registered, they recieve confirmation that they have successfully registered.

#### Epic 3 - User Login

**User Story - Account Sign In**

As a registered user, I can sign in with my username/password so that I can access the portal

- Acceptance Criteria 1  
As a registered user when I click log in and enter in the relevant log in criteria i should be logged into the website
- Acceptance Criteria 2  
If I am not a registered user and I try to log in I will see an error message of invalid credentials and will be prompted to register
- Acceptance Criteria 3  
Once the user is logged in, they recieve confirmation that they have.

**User Story - Reset forgotton password**

As a registered user, I can securely obtain Forgotten Password so that I can gain access if password is forgotten

There is a clear option visable to click if you have forgotten your password

- Acceptance Criteria 1  
There is a clear option visable to click if you have forgotten your password
- Acceptance Criteria 2  
Once nessesary information is given by user, there is a clear procedure to follow that results in acess being given 

#### Epic 4 - Studio booking system

**User Story - Edit Studio availability**

As a site administrator, I can CRUD available time slots so that clients can see when the studio is available

- Acceptance Criteria 1  
The administrator can create time slots in the admin panel.
- Acceptance Criteria 2  
The administrator can view time slots in the admin panel.
- Acceptance Criteria 3  
The administrator can update time slots in the admin panel.
- Acceptance Criteria 3  
The administrator can delete time slots in the admin panel.

**User Story - View Available Time Slots**

As a registered user, I can view available time slots so that I can decide when is best time to book

- Acceptance Criteria 1  
The user can see what time slots are available.

**User Story - Creating a new booking**

As a registered user, I can book a slot so that I can secure my place to use the studio.

- Acceptance Criteria 1  
The user can specify when they would like to use the studio.
- Acceptance Criteria 2  
The user can specify equipment requirements.
- Acceptance Criteria 3  
There is confirmation of the booking

**User Story - Viewing My Booking**

As a registered user, I can view my bookings so that i can choose what to do with them

- Acceptance Criteria 1  
The user can see all bookings that they have made
- Acceptance Criteria 2  
The user can modify any future bookings they have made
- Acceptance Criteria 3  
There is confirmation of the modification

**User Story - Cancel A Booking**

As a registered user, I can cancel my book so that I can let the studio know if I cannot make it

- Acceptance Criteria 1  
The user can cancel a booking they have made
- Acceptance Criteria 2  
There is a confirmation of the cancellation

#### Epic 5 - Recorded media Streaming

**User Story - Streaming/downloading my media**

As a registered user, I can stream and download any media that I have been involved with so that I can use the medai created

- Acceptance Criteria 1  
Registered user can navigate to folders and list of recorded media
- Acceptance Criteria 2  
User can stream there recorded media
- Acceptance Criteria 3  
User can download recorded media

**User Story - Uploading my Media**

As a site owner, I can upload recorded media so that the clients can strream or download

- Acceptance Criteria 1  
Site owner can navigate to area to upload media 
- Acceptance Criteria 2  
Site owner can upload media
- Acceptance Criteria 3  
Site owner can delete media
- Acceptance Criteria 4  
Site owner can modify media

#### Epic 6 - Enhancing Website Asthetics

**User Story - Design is consistent with existing site**

As a user, all areas of site should be consistant in appearance so that I have a great user experience.

- Acceptance Criteria 1  
When navigating between portal and existing website, they should look similar in design

**User Story - Design is responsive**

As a site user, I can easily navigate and view content using wide range of devices so that I have a great user experience

- Acceptance Criteria 1  
The layout automatically adjusts based on screen size and orientation
- Acceptance Criteria 2  
All elements such as text, images, buttons etc are easily viewed and visable on a range of devices
- Acceptance Criteria 3  
All navigation elements are optimised for touch devices














<!-- what would we like when visiting Studio Portal?
What kind of features would it provide its users?
1) The ability to create, Read, update and delete a booking for a recording session
2) the ability to stream and download rough mixes from recording sessions
3) signup process to be easy and frictionless

Problem statement: How do I develop a portal application that delivers this functionality to a user?

A user can view available time slots for the studio. 
A normal user is logged in they can access the portal content including: 
  1) Create, Read, Update and Delete bookings
  2)  View booking history
  3)  Stream/Download recordings made at studio
  4)  Manage their account settings

An Admin user can 
  1) Create, Read, Update and Delete bookings
  2) Create, read, Update and delete recordings -->

