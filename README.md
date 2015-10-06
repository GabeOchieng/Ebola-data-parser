
# Ebola-data-parser

PLEASE PREVIEW IN RAW FORMAT TO READ CLEARLY.

This is a python script that parses the Ebola data provided by the WHO through HDX database and converts it into a simple format that can be imported as a variable into MATLAB or Octave.

An example of expected input is in the following format:
header1, header2, header3 //first line contains headers for the columns
"Cumulative number of confirmed, probable and suspected Ebola cases",Guinea,2015-03-10,3285.0
"Cumulative number of confirmed Ebola cases",Guinea,2015-03-10,2871.0
"Cumulative number of probable Ebola cases",Guinea,2015-03-10,392.0
"Cumulative number of suspected Ebola cases",Guinea,2015-03-10,22.0
"Cumulative number of confirmed, probable and suspected Ebola deaths",Guinea,2015-03-10,2170.0
"Cumulative number of confirmed Ebola deaths",Guinea,2015-03-10,1778.0
"Cumulative number of probable Ebola deaths",Guinea,2015-03-10,392.0
"Cumulative number of confirmed, probable and suspected Ebola cases",Liberia,2015-03-10,9343.0
"Cumulative number of confirmed Ebola cases",Liberia,2015-03-10,3150.0
"Cumulative number of probable Ebola cases",Liberia,2015-03-10,1879.0
"Cumulative number of suspected Ebola cases",Liberia,2015-03-10,4314.0
"Cumulative number of confirmed, probable and suspected Ebola deaths",Liberia,2015-03-10,4162.0
"Cumulative number of confirmed, probable and suspected Ebola cases","Sierra Leone",2015-03-10,11619.0
"Cumulative number of confirmed Ebola cases","Sierra Leone",2015-03-10,8428.0
"Cumulative number of probable Ebola cases","Sierra Leone",2015-03-10,287.0
"Cumulative number of suspected Ebola cases","Sierra Leone",2015-03-10,2904.0
"Cumulative number of confirmed, probable and suspected Ebola deaths","Sierra Leone",2015-03-10,3629.0
.... //etc. till end of file.

Expected output (unrelated to input because of size constraints of the input file):
193 8428.0  //first part is the day since infection start, second part is selected metric
189 8389.0
188 8383.0
187 8353.0
185 8353.0
182 8320.0
181 8308.0
180 8289.0
178 8223.0
175 8223.0
174 8223.0
173 8212.0
172 8212.0
171 8199.0
168 8155.0
167 8138.0
166 8135.0
165 8135.0
161 8084.0
160 8063.0
159 8059.0
158 8059.0
