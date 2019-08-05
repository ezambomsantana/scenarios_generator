import os

scenario_name = "scenario3"
os.mkdir(scenario_name)

for x in range (0, 11):
  folder = scenario_name + "/" + str(x)
  os.mkdir(folder)
  for y in range(0,21):

    file1 = open(folder + "/config" + str(y) + ".xml","w") 
    file1.write("<scsimulator_config>\n")
    file1.write(" <config \n")
    file1.write("      trip_file=\"../" + folder + "/trips" + str(y) + ".xml\"\n")
    file1.write("      map_file=\"../" + scenario_name + "/network.xml\"\n")
    file1.write("      output_file=\"../output/events.xml\"\n")
    file1.write("      traffic_signals_file=\"../" + scenario_name + "/signals.xml\"\n")
    file1.write("      digital_rails_file=\"../" + scenario_name + "/empty-digital-rails.xml\"\n")
    file1.write("      simulation_time=\"86400\"/>\n")
    file1.write(" </scsimulator_config>")

    file1.close()

