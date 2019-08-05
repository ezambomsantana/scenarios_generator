for x in range(0,21):

  file1 = open("scenario-4-5/config" + str(x) + ".xml","w") 
  file1.write("<scsimulator_config>\n")
  file1.write(" <config \n")
  file1.write("     trip_file=\"../scenario5/trips" + str(x) + ".xml\"\n")
  file1.write("      map_file=\"../scenario5/network.xml\"\n")
  file1.write("      output_file=\"../output/events.xml\"\n")
  file1.write("      traffic_signals_file=\"../scenario5/signals.xml\"\n")
  file1.write("      digital_rails_file=\"../scenario5/empty-digital-rails.xml\"\n")
  file1.write("      simulation_time=\"86400\"/>\n")
  file1.write(" </scsimulator_config>")

  file1.close()

