import chili

# NO TOUCHY
file_name = chili.init_tr("10", "3.12.20")
# END NO TOUCHY


meetings = ["Meeting 1", "Meeting 2"]
chili.recent_meetings(file_name, meetings)


chili.new_section(file_name, "TASKS COMPLETED since last meeing")

chili.new_task(file_name,
			   "Really long Task title that is really long",
			   "3.3.33",
			   "3.3.33",
			   "100",
			   "Bob (85\\%) Fred (15\\%)",
			   "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
			   "Powering off can be done through the command line. RPi does not support WOL (Wake on Lan) through its ethernet ports so we needed to interface with the Ethernet Power Controller on site. Code complete and demonstrated in demo.")


# NO TOUCHY
chili.finish_the_chili(file_name)
# END NO TOUCHY