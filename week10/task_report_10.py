import sys
sys.path.insert(1, '../src/')
import chili

# NO TOUCHY
file_name = chili.init_tr("10", "3.27.20")
# END NO TOUCHY

# To add a meeting, put a string in the list ex. "Client meeting"
meetings = ["Client Zoom Meeting 3.27.20"]
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
               "Create a script to make these task reports easier to make",
               "3.25.20",
               "3.26.20",
               "100",
               "Peter (95\\%) Adam (5\\%)",
               "Write a python script that auto generates a pdf of the task report so we don't have to mess around with google docs' terrible copy and paste.",
               "Code written and tested and working.")

chili.new_task(file_name,
               "Investigate Deepstate for Testing APIs",
               "2.27.20",
               "3.16.20",
               "100",
               "Peter (100\\%)",
               "Investigate to potentially use deepstate fuzzing to test the various APIs for bugs",
               "At this time, deepstate is not easily available to the public, i.e. incredibly lacking in documentation, have to use docker(when there is a working image), etc.")


chili.new_section(file_name, "This week’s Tasks: Work plan for coming week")
chili.new_task(file_name,
               "User Manual",
               "3.27.20",
               "",
               "0",
               "Peter (50\\%), Rest TBD", # I am giving my self the percentage since I will be doing LaTeX
               "Create the user manual for the system to give to JC so they can replicate/use the system",
               "A manual for the system")

chili.new_task(file_name,
               "BrainCon Code Documentation",
               "3.27.20",
               "",
               "Trey (70\\%) Peter (20\\%) Adam (10\\%)",
               "Document the code to limit future questions about source code and to allow future developers to read and understand our code.",
               "Well-documented code.")

chili.new_task(file_name,
               "NeuronCon Code Documentation",
               "3.27.20",
               "",
               "Adam (34\\%) Mike (33\\%) Brandon (33\\%)",
               "Document the code to limit future questions about source code and to allow future developers to read and understand our code.",
               "Well-documented code.")

chili.new_task(file_name,
               "Circuit Diagrams",
               "3.27.20",
               "",
               "Adam (70\\%) Peter (30\\%)",
               "Create circuit diagrams for all of the curcuits made for the project to allow future EE's to improve and understand the electronics.",
               "Circuit diagrams")

cili.new_task(file_name,
              "Design Review 3",
              "3.27.20"
              "",
              "All",
              "Create some sort of presentation for Design Review 3, modified due to the covid-19 craziness",
              "A presentation for design review 3")

chili.new_task(file_name,
               "Convert code away from WiringPi",
               "3.13.20",
               "4.10.20",
               "11",
               "Michael (100\\%)",
               "WiringPi seems to conflict with the PWM PiGPIO lib. PiGPIO also supports GPIO access and does not use the WiringPi virtual numbering (which has only confused things).",
               "Code converted to setup with and use PiGPIO commands. Pushed to repo.")

chili.new_task(file_name,
               "Test pins after conversion to PiGPIO",
               "3.13.20",
               "4.10.20",
               "0",
               "TBD (dibs)",
               "Test that conversion to PiGPIO addresses the correct pins and outputs the correct signal.",
               "Code tested and confirmed to work.")

chili.new_task(file_name,
               "Utilize Thread Pool",
               "3.6.20",
               "3.29.20",
               "70",
               "Brandon (100\\%)",
               "The thread pool code compiles, must create a workflow and main method for using thread pool on NeuronCon",
               "A main.cpp file designed using the thread pool.")

chili.new_task(file_name,
               "Put together abstract for UGRADS",
               "2.21.20",
               "3.10.20",
               "0",
               "Adam (20\\%), Trey (20\\%), Peter (20\\%), Mike(20\\%), Peter (20\\%)",
               "Develop an adequate abstract for UGRADS",
               "Abstract is submitted")

chili.new_task(file_name,
               "Merge stepper code with piezo code and add networking",
               "3.6.20",
               "3.13.20",
               "0",
               "Trey (25\\%), Adam (25\\%), Brandon (25\\%), Mike (25\\%)",
               "To prepare for demo, merge all the separate tester files into one so that we can handle BrainCon packets for controlling both NAT and siderostat",
               "Raspberry Pi can receive a packet from BrainCon with info for motor_el, motor_az, nat_el, nat_az, and Pi can output counts to MotorCon and set PWM appropriately")


chili.new_section(file_name, "Upcoming Tasks: Planning")
chili.new_task(file_name,
               "Research and implement sending command line instructions from within C code",
               "3.13.20",
               "4.10.20",
               "0",
               "Mike (100\\%)",
               "It is useful (yet dangerous) to accept command line input from code. Research protocol in C and implement test code.",
               "Test code written and tested.")

chili.new_task(file_name,
               "Determine packet structure for including command line instructions.",
               "3.13.20",
               "4.10.20",
               "0",
               "Trey (50\\%) Mike (50\\%)",
               "Decide on a way to include, differentiate, and act on command line instructions within packet.",
               "Design determined.")

chili.new_task(file_name,
               "Implement the architected design for command line instructions",
               "3.13.20",
               "4.10.20",
               "0",
               "Trey (50\\%) Mike (50\\%)",
               "Trey will incorporate and differentiate the data. Mike will differentiate and execute the data.",
               "Data terminated.")

chili.new_task(file_name,
               "Create and document useful aliases for BrainCon",
               "3.13.20",
               "4.10.20",
               "0",
               "Mike (100\\%)",
               "Create useful system admin aliases for BrainCon to facilitate easy system maintenance.",
               "Aliases created and documented.")

chili.new_task(file_name,
               "NAT testing",
               "2.20.20",
               "3.10.20",
               "0",
               "All",
               "Test piezo functions and controls on a NAT at NPOI.  Since PiGPIO was chosen 3/5/20 and testing was accomplished on oscilloscope, can set up a test at NPOI now- to do testing need to contact Jason Sanborne or other available observers to set up the photon counters, these photon counters will tell us how our PWM changes are affecting the piezos",
               "We succeed in controlling a NAT or not.  We observe how voltage changes change the mirror positioning. We can now correlate AlignCon packets to voltage values")

chili.new_task(file_name,
               "Prepare for alpha prototype",
               "1.24.20",
               "3.16.20",
               "100",
               "All (proportional to individual parts and their contributions)",
               "Work on capabilities outlined in alpha prototype and be ready to present an acceptable alpha",
               "Testing and demonstration is performed")

chili.new_task(file_name,
               "AlignCon/ WasaMon packet value correlation",
               "1.24.20",
               "3.10.20",
               "0",
               " Peter (40//%),Trey (40//%)  Adam (20//%)",
               "AlignCon value conversion from x,y to voltages (adding or subtracting from current voltage value depending on photon counts and x,y offset value) and motor count conversion for WasaMon. This correlation is done through testing at NPOI through sending motor counts and observing the change",
               "AlignCon packets and WasaMon packets are correlated to voltage change and motor counts respectively through testing results")

# NO TOUCHY
chili.finish_the_chili(file_name)
# END NO TOUCHY

# Me touchy chili long time
# Me sssooo chili
