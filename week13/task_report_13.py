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
               "Capstone Presentation: Intro",
               "3.29.20",
               "4.10.20",
               "100",
               "Adam (100\\%)", 
               "Write script, make slides, and record Intro for Capstone Presentation",
               "Video of good quality sufficiently intros the background for the site.")

chili.new_task(file_name,
               "Capstone Presentation: Problem Overview",
               "3.29.20",
               "4.10.20",
               "100",
               "Peter",
               "Outline the current solution without bashing the previous hardware or mention satellite.", 
               "Video section recorded.")

chili.new_task(file_name,
               "Capstone Presentation: Solution",
               "3.29.20",
               "4.10.20",
               "100",
               "Mike",
               "Outline our solution and compare to existing setup", 
               "Video section recorded.")

chili.new_task(file_name,
               "Capstone Presentation: Schedule and Testing",
               "3.29.20",
               "4.10.20",
               "100",
               "Mike",
               "Overview of schedule. Detailed list of planned tests.", 
               "Video section recorded.")

chili.new_task(file_name,
               "Capstone Presentation: Challenges and Resolutions",
               "3.29.20",
               "4.10.20",
               "100",
               "Mike",
               "Tell the riveting story of our journey and all its trials and tribulations.", 
               "Video section recorded.")

chili.new_task(file_name,
               "Capstone Presentation: Future Work & Conclusion",
               "3.29.20",
               "4.10.20",
               "100",
               "Adam (100\\%)",
               "Write script, edit powerpoint slides, record video of this section",
               "Video of decent quality is added.")

chili.new_task(file_name,
               "Capstone Presentation: Edit video",
               "3.29.20",
               "4.10.20",
               "100",
               "Adam (100\\%)", 
               "Complete video presentation by splicing everyones sections together, editing audio levels, screen resolutions, and transitions",
               "Video of decent quality is put together.")

chili.new_task(file_name,
               "Capstone Presentation: Export and submit video mp4",
               "3.29.20",
               "4.10.20",
               "100",
               "Adam (100\\%)", 
               "Export a low-res and high-res version of the video- which takes a while- and submit to the drop box, also taking a while.  Resubmit to Drive according to Doerry's instructions",
               "Video is exported and submitted.")

chili.new_task(file_name,
               "Capstone Poster: Format template",
               "4.6.20",
               "4.15.20",
               "100",
               "Peter (100\\%)", 
               "Since Peter has another project which is also being submitted to UGRADS, develop a good template for where NPOI images and text boxes can go.",
               "Modified poster template is created.")

chili.new_task(file_name,
               "Capstone Poster: Make and format the poster",
               "4.6.20",
               "4.15.20",
               "100",
               "Adam (100\\%)", 
               "Make UGRADS Poster and submit to client for review. UPDATE client meeting 4/17 says to make big changes.",
               "Poster is created.")

chili.new_task(file_name,
               "Capstone Poster: Outline",
               "3.29.20",
               "4.10.20",
               "100",
               "Mike",
               "Outline of what sections to have in poster, layout, and order of discussion.", 
               "Outline distributed to team.")

chili.new_task(file_name,
               "Create and document useful aliases for BrainCon",
               "3.13.20",
               "5.8.20",
               "100",
               "Mike (100\\%)",
               "Create useful system admin aliases for BrainCon to facilitate easy system maintenance.",
               "Aliases documented, but not created on site.")


chili.new_section(file_name, "This week’s Tasks: Work plan for coming week")

chili.new_task(file_name,
               "Capstone Poster: Finalize",
               "4.15.20",
               "4.19.20",
               "0",
               "Adam (25\\%) Brandon (25\\%) Trey (25\\%) Peter (25\\%)", 
               "Based on feedback in client and mentor meeting, redo poster",
               "Poster is created and submitted to UGRADS")

chili.new_task(file_name,
               "UGRADS: Choose time for questions",
               "4.15.20",
               "4.17.20",
               "90",
               "All", 
               "Choose when we will accept questions from judges for UGRADS",
               "Time is submitted to UGRADS")

chili.new_task(file_name,
               "Client: Submit Preliminary As-Is", 
               "4.10.20",
               "4.22.20",
               "0\\%",
               "ALL",
               "Client needs As-Is report early to present to NRL in order to get funding for hiring us over the summer", 
               "Preliminary As-Is is sent to client")

chili.new_task(file_name,
               "UGRADS: Submit Additional Presentation", 
               "4.10.20",
               "4.22.20",
               "0\\%",
               "ALL",
               "Submit new video presentation to client for review before final submittion to UGRADS", 
               "Video is sent to client")

chili.new_task(file_name,
               "Client: Submit Moving Forward and Testing Plan", 
               "4.10.20",
               "4.22.20",
               "0\\%",
               "ALL",
               "To acquire funding from NRL -> Send client doc with testing plan + plan moving forward (things to implement, improvements to make, what we would do if we were to continue on this proect)", 
               "Best case scenario -> Moving Forward doc is sent to Client. Funding is secured. We have jobs, yay!")

chili.new_section(file_name, "Upcoming Tasks")

chili.new_task(file_name,
               "BrainCon Code Documentation",
               "3.23.20",
               "5.1.20",
               "10",
               "Trey (70\\%) Peter (20\\%) Adam (10\\%)",
               "Document the code to limit future questions about source code and to allow future developers to read and understand our code.",
               "Well-documented code.")

chili.new_task(file_name,
               "NeuronCon Code Documentation",
               "3.23.20",
               "5.1.20",
               "8",
               "Adam (50\\%) Brandon (50\\%)",
               "Document the code to limit future questions about source code and to allow future developers to read and understand our code.",
               "Well-documented code.")

chili.new_task(file_name,
               "Circuit Diagrams",
               "3.27.20",
               "5.1.20",
               "1",
               "Adam (60\\%) Peter (20\\%) Brandon (20\\%)",
               "Create circuit diagrams for all of the curcuits made for the project to allow future EE's to improve and understand the electronics.",
               "Circuit diagrams")

chili.new_task(file_name,
               "Finilaze Team Website",
               "4.8.20",
               "5.8.20",
               "90",
               "Adam (100\\%)",
               "Finalize website. Statically-link all imports so update doesn't break formatting. Add Contact Us page. Update all new docs and embed video of presentation.",
               "Website is finalized")

chili.new_task(file_name,
               "Final Product Acceptance Demo",
               "4.8.20",
               "5.8.20",
               "0",
               "ALL",
               "Final demonstration of solution. Discuss options with mentor due to site closure.",
               "Time and date for demo is set") 

chili.new_task(file_name,
               "User Manual: Raspberry Pi Setup",
               "3.23.20",
               "5.1.20",
               "0",
               "Adam (10\\%) Brandon (50\\%)", 
               "Create the user manual for formatting the OS, downloading dependencies, and running the embedded software",
               "Section is clear and concise")

chili.new_task(file_name,
               "User Manual: BrainCon Setup",
               "3.23.20",
               "5.1.20",
               "0",
               "Peter (50\\%) Trey (50\\%)", 
               "Create the user manual for things necessary for downloading, compiling BrainCon codebase",
               "Secion is clear")

chili.new_task(file_name,
               "User Manual: NeuronNet Init",
               "3.23.20",
               "5.1.20",
               "0",
               "Trey (100\\%)", # I am giving my self the percentage since I will be doing LaTeX
               "Create section for setting up the network for BrainCon and Raspberry Pi including IP addresses and libraries needed",
               "Section is clear")

chili.new_task(file_name,
               "User Manual: BrainCon GUI",
               "3.23.20",
               "5.1.20",
               "0",
               "Peter (50\\%) Trey (50\\%)", 
               "Create the user manual for how to run and use the GUI",
               "Astronomers can understand how to use the GUI")

chili.new_task(file_name,
               "User Manual: BrainCon Replication",
               "4.10.20",
               "5.8.20",
               "90",
               "Mike (100\\%)",
               "Document BrainCon linux installation, configuration, and additional package installs.",
               "Documentation such that even a mac boy like Adam can do it.")

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
