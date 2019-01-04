# The following works.
import tabula

source = "./data/2015 Data/"
file_name = source+ "Belmont.pdf"

# Referendum on Senior Services Renewal Levy: 127-129
# Ref. on Mental Hental Replacement and Decrease Levy: 130-132
# Ref. on Child Services Replacement Levy: 133-135
df_1 = tabula.read_pdf(file_name, pages=[127, 128, 129])
df_2 = tabula.read_pdf(file_name, pages=[130, 131, 132])
df_3 = tabula.read_pdf(file_name, pages=[133, 134, 135])
output_source = "./Ref_data_raw/"
df_1.to_csv(output_source + "Belmont_County_Senior_Services_Renewal.csv")
df_2.to_csv(output_source + "Belmont_County_Mental_Health_Services.csv")
df_3.to_csv(output_source + "Belmont_County_Child_Services.csv")
