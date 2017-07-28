# SEN 941 Software Engineering 1/Software Engineering Managment

***

### Class 1 - Lecture 1: The Software Proccess

* Fundamental assumption that good processes lead to good software and reduce risk

* Risk managment asks what can go wrong in a software project and how can risk be reduced?

* The general process is Feasability/Planning -> Requirements -> Design -> Implementation -> Operation/Maintance.  Requirments, design, and implementation is generally considered the software engineering process.  

* Waterfall model: Requirements def-> system/software design-> program/unit testing-> integration and system testing-> operation/maintenance.  Advantages of the waterfall model: Process visibility, dpeendence on individuals, quality control, cost control.  Disadvatnages: Each stage in the process reveals new understanding of the previous stages which requires the earlier stages to be revised.  

* Iterative development is intial implemetnation for user comment, followed by refinement until system is complete.  Vaporware: user interface mock-up, Throw away software components, dummy modules, rapid prototyping, successive refinement.  

* Completed projects should look like the waterfall model, but the development process is always partly evolutionary and risk is decreased through prototyping components, dividing development into phases, following a transparent software process, making use of reusable components.  

* Fesability study usually looks at the client, the scope, benefits, resources needed, potential obstacles/risks and how they can be minimized

* THe feasability leads to a decision 

***

### Lecture 2: Developing Requirements/System Model

* Domain Analysis is the process by which a SWE learns about the domain to better understand the problem.  THe domain is the generalf field of business/tech in which the clients w. use the software.  A domain expert is a person who has a deep knowledge fo the domain.  

* Defining the problem/scope.  A problem can be expressed a a difficulty users/customers are facing or as an opportunity that will resutl in some benefit such as improved productivity/sales.  

* Defining the scope.  Narrow the scope by defining a more precise problem (List all the things you might imagine the system doing, exclude things if they are too broad, and determine high level goals if things are too narrow)

* A requirement is a statmeent about the propsed system that all stakeholders agree must be made true in order for the customers problem to be solved adequatley.  (Short and concise, says somethign about the system, All stakeholders have agreed it is valid, helps solve the problem).  A collection of requirments is a requirements document.  FUnctional requirements describe what the system should do.  Non-functional requriements are constraints that must be adhered to during development.  

* Functional requirements are things like what inputs the system should accept, what outputs the system should produce, what data the system should store that other systems might use, what computations the system should perform along with its timing and synchronization

* Main types of non-functional requirments usually affect usability, efficency, reliability, maintainability/reusability including response time, throughput, resource usage, reliability, availability, recovery from failure.  Other categories are the environment/tech stack/plathform and also project plan/development methods and methodology including cost/delivery date.  Usually the requirmenets docs is a list a features to include.  

* Techniques for gather/analysing requirements are observation (read docs/discuss requirements w/ users, shadowing users), interviewing asking specific details, future vision, alternative ideas, diagrams.  Brainstorming is another way to analyse requirments but usually you want an experienced moderator, decide on a trigger question and start a discussion from there.  Protyping is another method which usually has mockups which do not access any databases etc... but is just a look alike

* There are two different types of requirement docs, the requirments (describes the system almost as a narrative and what will happen/how it will happen).  THe specification goes into EXCRUTIATING detail and can be hundreds of pages long.  The level of detail depends on the size of the system, the need to interface w/ other systems, the audience, stage in requirments gathering, level of experenice w/ the domain/tech, the cost that would be incurred if requirments were faulty.  

* Each reqirument shoudl have benefits that outwigh costs, be important for the solution of the problem, be clear/consistent and unambiguous, be realistic, verifiabile, identifiable, does not over constrain the system.  

* The reqs document should be sufficently complete, well organized, clear, and agreed to by all stakeholders, and traceable (e.g. when there are changes in the reqs the req doc version # is updated).  

* The reqs document should follow the flow of 1.  Problem, B.  BG info, C.  Envrio/sys tmodels, D.  Functional Reqs E.  non-functional reqs.

* Reqs change because of biz processes or tech changes, problems become better understood, and reqs analysis never stops and happesn via interacting w/ clients/users and consistenly analyze the benefits/costs of the system.  Avoid making a system bigger, try and make it better.  

* Difficulties in requirment analysis include lack of understanding in the real problem, requirments shifting, doing too much at once, imprecise requiremnts.  The usual flow of a reqs process is a feasability study to reqs analysis, to reqs definition, to reqs specifiction.  

* Requirments specs have purpose including describing reqs to stakeholders expressed in terms tehy understand and from mutlpile viewpoints.  It also describes the reqs to the implementers to be as specific as possible, and expressed in relatable/understandable terms so as to be comprehensive.  It also sets clear documentation and functions as a contract.  

* The following is an example of an SRD (Software Requirments Document) (page 25 of the course book)

```

SOFTWARE REQUIREMENTS DOCUMENT (SRD) 


1.	Scope
The SRD covers those requirements pertaining to the interface, internal operation, and reporting functions of the XYZ program.
1.1	Identification
This document covers version 1.0 of the XYZ program. At this time a formal name has not been identified for the program module.
1.2	System Overview
The XYZ program is designed to provide DAP personnel, managers and software developers with a means to ascertain if specific address records are contained in the XYZ loadables.
2	Referenced Documents
None at this time.
3	Requirements
3.1	General
The program shall be developed as a 32-bit Windows application using Visual C++ version 6.0.
The program architecture shall support the multiple document interface metaphor.
The program shall contain a context sensitive Help facility.  
Context sensitive help shall be provided at the screen and menu levels.  It is not necessary to provide context sensitive help at the data element input level.
The program shall store user define parameters in a parameter file that can be modified by any ASCII text editor.
Upon startup the program shall attempt to read and make use of the parameter file.
The program shall validate entries in the parameter file and report to the user if an existing parameter is no longer valid.
3.2	User Interface - Parameter Settings
The program shall make use of a tab property sheet metaphor accessible from a drop down menu for user defined program settings.
A "General" property sheet tab shall be created to allow the user to define and store directory settings for basic program operation that include local XYZ directory location and output log/report directories.  An example of this type of property sheet is available in the Appendix, labeled Screen Shot #1.
A "Network" property sheet tab shall be created to allow the user to define and store network settings, user name and password for access to the XYZ loadables, and the NDSS location of XYZ loadables. An example of this type of property sheet is available in the Appendix, labeled Screen Shot #2.

3.3	User Interface - Refreshing Directories
The program shall utilize a dialog box accessible from a drop down menu that provides the user with a means of selecting how the local refresh on their PC is to occur.  An example of this dialog box is available in the Appendix, labeled Screen Shot #3.
The dialog box shall provide the user with an option of refreshing from the NDSS platform, a local drive/directory, or from a networked drive/directory.
All refresh options are to present confirmation dialog boxes to the user before the action takes place.
All refresh options must first determine whether the destination has enough available free space before the action takes place.
The option to refresh from the NDSS must echo to the user the TCP/IP address of the NDSS machine and the directory on the machine of where the XYZ loadables are located.  This information is to come from the parameter settings supplied by the user in previous program options.
Due to inconsistent FTP problems, the refresh option may have to include a means of transferring data from the NDSS to the VAX Cluster via DECNet "COPY" commands, then an FTP session from the VAX Cluster to the user's local machine.
The dialog box shall display the target locations of the users local machine of where the information will be located once a refresh occurs.
3.4	Address Record Lookup Functions
The program shall provide the means for the user to specify whether they are looking for a POB, RRT of SFB record.
The program shall provide a further depth of options for SFB records that include Firm, Street and Building.
Input for POB records shall include a distinct field for box numbers.
RRT record lookup shall allow the user to specify whether they are looking for a Rural Route or a Highway Contract record.
Input for RRT record lookup shall include a distinct field for route or highway contract numbers.
SFB record lookups shall provide distinct input fields for house/street number, pre-directional, suffix and post-directional data, as well as the street, building or firm name field.
Street, building and firm names are to be normalized before they are sent for lookup by using keyword routines from the Normalization Phase of XYZ Directory Generation.
Output & Report Requirements
TBD
Directory Test Functions
TBD
3.7	Internal Program Specific Requirements
The user interface portion of the program shall be separated from the processing or lookup function of the program.
The directory access and lookup functions of the program shall be written in standard ANSI C.
The directory access and lookup functions of the program shall be written in a manner that will allow the code to be ported from a Windows based environment to a VAX Alpha based environment.
3.8	Security and Privacy Protection Requirements
There are no specific security and privacy requirements outside of those normal requirements governing use of XYZ data and systems.
3.9	Computer Resources.
The XYZ program shall be designed to run on an INTEL 586 or greater machine with an NT 4.0 operating system.
The platform must contain at least 128 megabytes of RAM.
There should be sufficient free space (over 400 megabytes) to hold the XYZ loadable directories.
The machine should have sufficient additional free space in order for swap space settings to be increased to 200 megabytes.
3.10	Software Quality Factors
All code written shall adhere to ESGI's internal coding standards.
The Windows front end of the program shall follow Microsoft Windows programming standards and conventions.
All error messages must be clear and concise.
All error messages must provide the user with information on a possible solution to the problem.
Error checking must be performed on all input and output actions.  Specifically, the program must verify the existence of input/output directories and data files as well as their accessibility regarding READ, WRITE, and UPDATE.
3.11	Design & implementation Constraints
[Describe any existing constraints on the design and implementation of the application (e.g. standards, growth, or changes in technology).]
3.12	Personnel Related Requirements
There are no specific personnel related requirements.
3.13	Training Related Requirements
There are no specific training related requirements.
3.14	Logistics Related Requirements
[Describe requirements on system maintenance, software maintenance, system transportation modes, supply-system requirements, impact on existing facilities, and impact on existing equipment.]
3.15	Other Requirements
No other requirements have been identified at this time.

3.16	Packaging Requirements
The XYZ program shall be delivered via an installation kit created by the latest version of Install Shield Express.
The installation kit shall be formed as a single self-extracting .EXE file. 
The installation kit shall be produced on CD-ROM and shall include a sample set of XYZ loadables.  The XYZ shall not be part of the self-extracting .EXE file.
The installation media shall include a "README" text file that instructs the user how to install the software and what the installation kit contains.
The installation kit shall present the user with a default set of installation directories and parameters.
The installation kit shall allow the user to change the default program installation location.
3.17	Precedence and Criticality of Requirements
At this time the precedence and criticality of requirements has not been ascertained.
4	Notes
[Include any pertinent general information such as background information, glossary, or rationale.  This includes acronyms, abbreviations, terms and definitions.]
5	Appendices

Screen Shot #1
Screen Shot #2
Screen Shot #3


```


***

Class 2 - Lecture 3: Requirements and Design

* Requiremnts should state what the system should do and the design should describe how it does this.  Design/requriements are inseperable.  

* The reqs decomuent is the offical statement of what is required of the developers and should have a definitions/descriptiion section.  There is an IEEE standard for a reqs document

* The design document states how a system should do something, a requirements document states what a system should do.  

* There are a number of models to use for design models including object oriented models, procedural models (flowchart), psuedo code, etc...

* Reqs analysis shoudl make minimal assumptions about system design, but the reqs definition must be consisting with tech/resources available, and in practice analysis/design are interwoven.  

* An addtional method is scenario planning which are descriptions of how a system is used in practice (user stories).  Scearios are helpful in reqs elicitation as people can relate to these more readily than abstract statement of what they req from a system.  Scenarios are useful for adding detail to an outline req description.  

* Use cases are based in UML which identify actors in an interaction and which describe the interaction itself and describes a set of use cases which should describe all possible intractions w/ the system.  Sequence diagrams may be sued to add detail to use cases by showing the sequence of event processing in the system.  

* After requrierments comes syte system deveopment stage with an analysis document which contains sytem models/diagrams/flow charts and design documents which contains the blueprint for the system design implementation. 


***

Class 2 - Lecture 4: System Model/The Analysis Stage

* System models are abstract descriptions of a ssytem whose requirements are being analysed

* The objectives of modeling include helping the analyst to understand the system functionality, and provide different models of the system from different perspectives including an external perspective(showing the system context/enviro), functional perspective(showing the system functionality), and structural perspective(showing the system data/architecture)

* Models have weakensses including not being able to model non functional system reqs and they don not usually include info about wether a method is appropriate for a given problem.  Models may also produce too much documentation, and system models are sometimes too detailed/difficult for users to understand.  

* System analys has methods for data modeling/design which are often entity/relationship diagrams, data flow diagrams, data dictionaries, object models/flow charts, many of these methods blur the distinction between analysis/design.  

* Different model types include dta proccessing modeling(shows how dta is proccessed in different stages), architectural model(showing main sub systems), response model(showing system reactions to events).  

* Context models are used to illustrate the boundries of a system and show the system and its relation to other systems.  

* Data dictionaries are lists of all the names used in system models.  Descriptions of the entities, relationships and attributes are included (this could become a DB).  This usually has a brief definition (e.g. what is a date), what it is (number/relation), where it's used(source, used by, etc...), may be combined with a glossary.

* Object models describe the system in terms of object classes, an objec class is an abstraction over a set of object w/ common atttributes and the servies/operations provided by each object.  There are various object models including inheritance and interaction models.  Object models are a natrual way of relflecting real world entitites, and more abtract entiteis are more difficult to model using this approach and requires a deep understanding of the application domain.  THis also requires strucuring the system into a set of coupled objects w/ well defined interfaces.  Object oriented decomposition is concerned w/ identifying object classes, their attributes/operations.  Objects can be created from these classes, and some control model used to coordinate object operations.  

* Entity relationship modeling is a DB or system of entities/relations, and is a tool for displaying/manipulating entity relation diagrams as well as tools for manipulating a DB/data storage system

* The importance of mddeling is that it is a simplification of reality and allows us to better understand the system, and allows us to simplify/abstract things.  Models can be formal or informal, the more complex the proejct, the more valuable a formal model becomes.  The chocie of what models to create influcens hwo the problem is solved, and every model can have different percision levels.  The best models are connected to reality, and the best design docs use/implement multiple models.  

***

Class 4: Lecture 5: Entity Relationship Modeling

* Technique for carrying out the conceputal/logical system design which has 3 basic notions of entities(like objects), attributes, and relationships

* An entity is an object that can be identifed in the users work enviro and that users want to track

* An entity is a thing/object in the real world w/in the application context and has a set of properties which uniquely identify it.  

* An attribute describes a charactersitc of an entity (e.g. an employee that has the attributes of a name, extension, date of hire, etc...)

* Relationships are associations between entities which express some r/w relationship.  Project and employee PARTICIAPATE in the employs relationship.  THe function that an entity plays in a relationship is called the entitys role

* Sets of relationships if there are more than one relationship between entities, there can also be recursive relationship that define/indicate roles for clarity.  A relationship can also have descriptive attributes.  

* Degree of relationships are the number of entitites participating in a relationship.  
* Cardinalities are the nubmer of entities to which another entity can be associated via a relationship.  E.g. one to one, one to many, many to one, many to many (e.g 32 seats to a bus would be one to many) (e.g. a person has 1 book, a person can onwn many cars but the cars only have one owner, a person can own many houses and a house can have multiple owners)

* Design issues are figuring out if something should be an entity or an attribute (e.g. location), and there is also an issue deciding eneity or relationship.  The general rule is that relationships for actions between entitites and whatever makes sense the the context of the application.  

* Entity/Relationships design starts at identifying the entity sets, and then describing the entity sets w/ attributs, and then specifying relationships and cardinalities

* A quick example is that every department w/in a company is in one division, and each divsision has multiple department that has multiple employees

* AN example of a many to many relationship is that any one supplier might supply more than one part, and any one kind of part might be bought from a different number of suppliers

* For the project implement a reqs doc

### Class 4: Lecture 6: Data Flow Modeling

* Data flow modeling is based on the notion that systems can be modeled as a set of interacting fuctions and uses data flow diagrams to graphically represent the external entities, prcesses, data flow, and data stores.  It is a graphical system model that shows all of the main requirments for an information system(inputs, outputs, proccesses, and data storage).  

* A terminator is an external entity w/ which the program system communicates, and is typically a person/group of people, and outside org or an agency.

*  Data flow diagrams are usually used together with proccess in that data flows are used to connect processes indicating that data items are moving from one process to another

* A data flow in a DFD should carry one type of information. Do not name a data flow too generic such as student, professor, administration.  A data flow can carry multiple items/composite items, and data flows should show directions  

* Data flows do not answer procedural questions

* A store describes a single or a set of data itmes(ex: a file, a DB, etc.. can be modeled as a store)

* Stores are connected to processes by data flows A data flow to a stroe FROM a process means writing an update of the store.  A data flow from a store TO a proccess means a READ of the store by the process.

***

Class 5: Lecture 7: System Analysis Object Oriented Design

* Object orieinted analysis/design uses visual reps similar to strucutred analysis, diagriming builds from ERD/DFD concepts, easy to learn and uses UML standards

* OOD Methodology is a reaction to shortcomings in structured analysis which was a problem of larger products, and data/action are treated as equal partners

* Object oriented analys with an object consisting of data(attributes, state, instance variables, fields, data memobers) and actions(methods/member fuctnons).  Objects are independent unit with conceptual/physical independence

* There are multiple OO methods (much like Agile KANBAN, etc...), all are essentially equivalent, and most use UML diagrams

* Three steps of OOA is 1.  Use case modeling(determine how various results are computed, this step is largely action oriented), 2.  Class/object modeling(determine classes/their attributes, this is data oritnted) 3.  Dynamic modeling(determine the actions performed by/or/to each class, this is action oritned).  The whole process is iterative

* Use case modeling for OOA can be represented graphicall or as a series of steps

* Class modeling is done by extracting classes/their attributes, represent them using an entity relationship diagram(ERD), deduce the classes from use cases/their scenarios, often there are multiple scenarios.  

* There are 2 approaches to class modeling which are noun extraction and CRC cards (requires domain expertise)

* Noun modeling is defining the problem/product in a single sentence.  Identify nouns is an informal strategy and create classes based off of ones that are similar, and generally the smallest number possible.  

* Iteration is needed to mature/provide more specificity (this is why there are so many iterative models e.g. waterfall, agile, etc...).  

* CRC cards stands for Class, Responsibility, COllaboration, which covers the name of the class, the functionality, and list of classes it invokes respectively.  The strength is that when acted out by team members CRC cards can highlight missing/incorrect itemls, but the weakness is that domain expertise is needed.  

* Dynamic modling is creating a UML state diagram which covers state, event, and predicate are distributed over the state diagram

### Class 5: Lecture 8: UML Diagrams

* UML is Unified moldeling language which serves as a bridge between reqs specs and the implementaiton and privdes a means to spec/document the design of a sotware system and is sutied for OOP design.  

* The notation for classes is having the name at the top, attributes in the middle, and operations/methods at the bottom.  Don't put anything in the diagram that doesn't need to be there.  The class notation is a description of a set of objects that share the same attributes, operations, relationships, and semantics.  

* The interface notation is a circle that specifies a servce/class or component e.g. the externally visible behavior of the element.  

* Interfaces are a set of rules for methds/things to be implemented

* THe notation for collaboration/use cases.  A collaboration defineds an  interaction(e.g. a society of roles) and elements that work together to provide some cooperative behavior.  A use case is a description of a set of sequences of actions that a system performs that yeilds a result.  

* An active class is a class whose objects own one or more process/threads and therefore can initiate control activity. 

* A componenet is a replaceable part of a system that conforms to/provides the relaization of a set of interfaces(e.g. packages), where a node is a phyiscal element that exists at runtime and represents a computational resource (such as a server) 


* An interaction is a behavior that comproises a set of messages exchanged among a set of objects witghin a particular context to accomplish a purpose.  A state maching is a behavior that specifies the sequence of staes an object/interaction goes through during its lifetime in response to events.  

* A package is a mechanism for organizing elements into groups (different package than Java type etc...).  A note is a symbol for rendering constraints/notes to elements.  

* A dependency is something representing a relationship between two things (an association)

* A generalization is a specalization/generalization relationship is which objects of the specialized elment(child) are subsitiutable for objects of the generalized element(parent).  A relization is a semantic relationship between classifiers wherein one clasifier spcifies a contract that another classifier carries out.  

* A diagram is the graphical representation of a set of elements usually rendered as a connected graph of verticies(things and relationships).  Class diagrams show a set of classes, interfaces and collaborations w/ their relatinships.  Objects show objects and their relationships.  Basically different diagrams emphasize different things (Interactions show how things are related, sequence diagrams emphasize time ordering, ocllaborationd diagrams emphasize organizition)


***


### Class 6: Lecture 9: OOD 2

* It's best to think LT and think of what would happen if your software were to be in use 5 years from now

* Reququirements give you a what, hte design gives you the how

* For Object design we begin to implement design ideas specificying responsibilites, attributes, operations, etc...

* One method to identify classes is noun identification, and then identify classes based off of that and any neccessary relationships and operations/methods (e.g. a book is an item in a library )

* THere is no single correct design, because druing the design proccess, elements may be hidden for simplication, elements may be missing, the model may not be consistent

* There are many levels of abstraction, high levels of abstraction show the overall syste, where low levels of abstraction are needed fro implementation.  Model entire systems at the same level of abstraction, but show diagrams w/ different level sof detail

* Scenarios, use cases, actors, and roles are another from of diagrams/explanation/narrative

* For the development cycle use cases are important, intuitive, but are often hard to translate into class models, but can help validate the design

### Class 6: Lecture 10: UML vs. ERD

* UML in not a replacement for Entity relationship diagramming.  UML does have its drawbacks b/c they can be more cluttered/less easily understood

* An entity relationship dagram can be mapped to a UML diagram.  

* UML notation includes the role that each object in the class is assuming in the relationship expressed w/ a noun on each side, but ERD diagrams do not

* In UML you can show a recursive relationship far easier, and in UMLs there are comments, UML usually shows more directionality than ERDs 

* Generalizations are more flexible in UML than they are in ERDs.  THere need not be only one generalization structure from a given class, you can have multiple generalizations in the same class.  (A generalization is basically a label/classification that is able to be connected/related to something else)

* UML allows for the creation of multiple relationship types beyond entity/class relationships including interaction, sequence, collaboration, activity, and state chart diagrams

* IN UML a component si a distributable piece of implementaion of a system including code (source, binary, or execuable).  This analgous term in an ERD is a subsystem, which is a grouping of elements that specifies what part of a system should do.  In other words a component can be thought of as an implementation of a subsystem.  

### Class 7: Lecture 11: Software Testing

* THe objective of testing is to executue a program to find errors, create a good test case that has a high probability of finding errors, and a good test finds a new error

* The two types of testing are black box and white box

* Black box testing is testing to make sure that the functionality is working correctly, given the correct inputs, what can you do from the outside to change the system, what is the output.  

* White box testing hcecks the code, tests the codntionals, loops, branches etc... The status is examined in terms of expected values.  It will often test important data strucutres/paths.  Black box testing is easier/more straightforward

* Unit testing is generally all white box, Integration testing is done by prorammers as they integrate code into the code base and is usually white box and some black box, Functional/System testing is usually done by an external group and is usually black box, Acceptance testing is usually done by the customer/rep and is certainly black box

* The testing process is usually designing test cases, executing the cases, preparing the test data, loading the test data, running the program w/ test data, testing the results, compare results to test cases, and report the test cases

* Planning a black box test case is putting and ID of the test case, describing the input conditions, describign the expected results, recording the actual results (this is known as the testing grid)

* The inputs and expected results must be specific (not just 'a passing grade', but define the percentage/what you want)

* There can also be failure test cases, (e.g. what happens if you're expecting an integer but they give you a character), or if the customer takes an illogical path, mandator fields aren't entered?, the program is suddenly stopped/interrupted?

* In testing, one input should lead to one output (one to one testing) 

* Verification/Validation, Verification asks if the product is being built correctly (E.g. the software should conform to spec), validation is asking if the correct product is being built(e.g. do what the user needs)

### Class 7: Lecture 13: Software design/THe design spec doc 

* NOTE: LECTURE 12 WAS SKIPPED BECUASE IT WAS THE MIDTERM REVIEW

* Design is a problem solving process whose objective is to find and describe a way to implment functioal requriemnts while respecting the constraints imposed by non fucntional requirments and while adhering to general principles (A design doc is a blueprint)

* A component is a piece of software/hardware that has a clear role, can be isolated/replaced, and are often designed to be reused, others may be specualized

* Modules are a component that is defined at the programming language level (e.g. packages)

* A system is a logical entity that has a set of definable responsiblities/objectives that consists of hardware/software, Systems can have specs whech are implemented by a collection of components, A system continues even if its components are changed/replaced, The goal of requrements analysis is to determine the responsiblities of a system.  A subsystem is a part of a larger system

* Top down design 