import sys
sys.path.insert(1, '../src/')
import chili

# NO TOUCHY
file_name = chili.init_tr("12", "4.10.20")
# END NO TOUCHY

# To add a meeting, put a string in the list ex. "Client meeting"
meetings = ["Client Meeting 4.10.20"]
chili.recent_meetings(file_name, meetings)

# Adding a new task
# chili.new_task(file_name,
#                task title,
#                initiation date,
#                due date,
#                status,
#                who, WARNING - put \\ before % sign
#                description,
#                outcome)
chili.new_section(file_name, "TASKS COMPLETED since last meeing")

chili.new_task(file_name,
               "Order Pi Parts \\& Laptop",
               "3.27.20",
               "3.30.20",
               "100",
               "Adam (100\\%)", 
               "Contact Henrique to order new Pi, laptop, sd card, and Pi case",
               "Parts are ordered")

chili.new_task(file_name,
               "Make changes to UGRADS abstract",
               "3.23.20",
               "4.6.20",
               "N/A",
               "",
               "No one had any comments on this, so I (Adam) left it as it is...",
               "Abstract was not edited")

chili.new_task(file_name,
               "Capstone Presentation Dry Run: Intro",
               "3.29.20",
               "4.10.20",
               "50",
               "Adam (100\\%)", 
               "Write script, make slides, and record Intro for Capstone Presentation Dry Run",
               "Video of good quality that does a good job of telling our story.")

chili.new_task(file_name,
               "Capstone Presentation Dry Run: Solution",
               "3.29.20",
               "4.10.20",
               "100",
               "Mike",
               "Outline our solution and compare to existing setup", 
               "Video section recorded.")

chili.new_task(file_name,
               "Capstone Presentation Dry Run: Problem Overview",
               "3.29.20",
               "4.10.20",
               "100",
               "Peter",
               "Outline the current solution without bashing the previous hardware or mention satellite.", 
               "Video section recorded.")

chili.new_task(file_name,
               "Capstone Presentation Dry Run: Schedule and Testing",
               "3.29.20",
               "4.10.20",
               "100",
               "Mike",
               "Overview of schedule. Detailed list of planned tests.", 
               "Video section recorded.")

chili.new_task(file_name,
               "Capstone Presentation Dry Run: Challenges and Resolutions",
               "3.29.20",
               "4.10.20",
               "100",
               "Mike",
               "Tell the riveting story of our journey and all its trials and tribulations.", 
               "Video section recorded.")

chili.new_task(file_name,
               "Capstone Presentation Dry Run: Future Work \\& Conclusion",
               "3.29.20",
               "4.10.20",
               "50",
               "Adam (100\\%)", 
               "Write script, edit powerpoint slides, record video of this section",
               "Video of decent quality.")

chili.new_task(file_name,
               "Capstone Presentation Dry Run: Compile all video together",
               "3.29.20",
               "4.10.20",
               "100",
               "Adam (100\\%)", 
               "Complete video presentation by splicing all videos together, editing audio levels, screen resolutions, and put together final version of dry run",
               "Video of decent quality is put together.")

chili.new_task(file_name,
               "Software Testing Doc",
               "3.29.20",
               "4.1.20",
               "(99, 100)",
               "All",
               "The software document is completed.", 
               "A super great document about testing.")


# TODO: CHANGE DATES TO AVOID RED FACE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! (to be read with a falling voice)
chili.new_section(file_name, "This week’s Tasks: Work plan for coming week")

chili.new_task(file_name,
               "Communicate with client our plan of action for the remainder of the term.",
               "4.2.20",
               "4.10.20",
               "10",
               "Adam (100\\%)",
               "Discuss plan of action with client so we are all on the same page.",
               "Discussed how to balance our efforts given the on-site restrictions and multiple upcoming deadlines (busy work intended for web app teams).")

chili.new_task(file_name,
               "Client: Submit preliminary poster for review",
               "4.10.20",
               "4.15.20",
               "0\\%",
               "ALL",
               "Client would like to look at the poster that we have worked on to give feedback", 
               "Poster is sent to client")

chili.new_task(file_name,
               "Client: Submit Preliminary As-Is", 
               "4.10.20",
               "4.22.20",
               "0\\%",
               "ALL",
               "Client needs As-Is report early to present to NRL in order to get funding for hiring us over the summer", 
               "Preliminary As-Is is sent to client")

chili.new_task(file_name,
               "Client: Submit Moving Forward and Testing Plan", 
               "4.10.20",
               "4.22.20",
               "0\\%",
               "ALL",
               "To acquire funding from NRL -> Send client doc with testing plan + plan moving forward (things to implement, improvements to make, what we would do if we were to continue on this proect)", 
               "Best case scenario -> Moving Forward doc is sent to Client. Funding is secured. We have jobs, yay!")

# @Brandon we can move this to removed or you can mark as complete. Just change the date!
chili.new_task(file_name,
               "Utilize Thread Pool",
               "3.6.20",
               "4.20.20",
               "90",
               "Brandon (100\\%)",
               "The thread pool code compiles, must create a workflow and main method for using thread pool on NeuronCon",
               "A main.cpp file designed using the thread pool.")


chili.new_section(file_name, "Upcoming Tasks")

chili.new_task(file_name,
               "Create and document useful aliases for BrainCon",
               "3.13.20",
               "5.8.20",
               "0",
               "Mike (100\\%)",
               "Create useful system admin aliases for BrainCon to facilitate easy system maintenance.",
               "Aliases created and documented.")

chili.new_task(file_name,
               "User Manual",
               "3.23.20",
               "4.24.20",
               "0",
               "Peter (50\\%), Rest TBD", # I am giving my self the percentage since I will be doing LaTeX
               "Create the user manual for the system to give to JC so they can replicate/use the system",
               "A manual for the system")

chili.new_task(file_name,
               "BrainCon Code Documentation",
               "3.23.20",
               "4.24.20",
               "2",
               "Trey (70\\%) Peter (20\\%) Adam (10\\%)",
               "Document the code to limit future questions about source code and to allow future developers to read and understand our code.",
               "Well-documented code.")

chili.new_task(file_name,
               "NeuronCon Code Documentation",
               "3.23.20",
               "4.24.20",
               "2",
               "Adam (34\\%) Mike (33\\%) Brandon (33\\%)",
               "Document the code to limit future questions about source code and to allow future developers to read and understand our code.",
               "Well-documented code.")

chili.new_task(file_name,
               "Circuit Diagrams",
               "3.27.20",
               "4.24.20",
               "1",
               "Adam (70\\%) Peter (30\\%)",
               "Create circuit diagrams for all of the curcuits made for the project to allow future EE's to improve and understand the electronics.",
               "Circuit diagrams")

chili.new_task(file_name,
               "Finilaze Team Website",
               "4.8.20",
               "5.8.20",
               "90",
               "Adam (100\\%)",
               "Ensure website defeats that of all other teams both now and who have come before.",
               "Other teams defeated and in disbelief (\"woah did it just resize?!?!?\".") # quotes in quotes may cause issue

chili.new_task(file_name,
               "Capstone Poster",
               "4.8.20",
               "5.8.20",
               "0",
               "ALL",
               "Create poster for our project and submit with 20 min video.",
               "Poster created and video recorded; assignment submitted (emphasis on first three letters).") 

chili.new_task(file_name,
               "Final Product Acceptance Demo",
               "4.8.20",
               "5.8.20",
               "0",
               "ALL",
               "Final demonstration of solution. Discuss options with mentor due to site closure (do in summer).",
               "Team and mentor have come to a reasonable agreement and set time to demo in summer.") 

chili.new_task(file_name,
               "Final Ass Built Report",
               "4.8.20",
               "5.8.20",
               "0",
               "ALL",
               "Write yet another report filled with the abbreviation of bachelor of science.",
               "Team and mentor have come to a reasonable agreement and set due dates for the summer (donuts upon request).") 

chili.new_task(file_name,
               "Final Delivery",
               "4.8.20",
               "5.8.20",
               "0",
               "ALL",
               "Just when you thought there could be no more, another assignment surfaces and restores anger to the population.",
               "Team and mentor have come to a reasonable agreement and set due dates for the summer (VEGAN donuts upon request).")

'''chili.new_task(file_name,
               "AlignCon WasaMon packet value correlation",
               "1.24.20",
               "TBD",
               "0",
               " Peter (40//%),Trey (40//%)  Adam (20//%)",
               "AlignCon value conversion from x,y to voltages (adding or subtracting from current voltage value depending on photon counts and x,y offset value) and motor count conversion for WasaMon. This correlation is done through testing at NPOI through sending motor counts and observing the change",
               "AlignCon packets and WasaMon packets are correlated to voltage change and motor counts respectively through testing results")'''

# NO TOUCHY
chili.finish_the_chili(file_name)
# END NO TOUCHY

# Me touchy chili long time
# Me sssooo chili
# LOL!
