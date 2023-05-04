# install the readxl package if !installed
install.packages("readxl")

# load readxl lib
library(readxl)

# specify the Excel spreadsheet file path
file_path <- "example.xlsx"

# read Excel spreadsheet into data frame
df <- read_excel(file_path)

# specify the file path for the CSV file
csv_file <- "example.csv"

# write the data frame to a CSV file
write.csv(df, file = csv_file, row.names = FALSE)
