In the dataset for this project, data related to the characteristics of each of area of Los Angeles in 2010 is shown.

This data are: the zip code number, number of inhabitants in the area, average age and the number of male and female 
inhabitants. In addition, it is also provided the number of households in a certain zip code and the average size of 
these properties indicated in squared meters. Finally, two more columns have been added with data of the string type, 
one indicates the type of area where the address is located (mountain, city or beach) and the last one shows the 
name of the neighborhood or district.

As we can see, each data set is related to some area of this city. Each area is marked with a zip code, moreover, one 
or more areas make up a neighborhood or district so, a neighborhood can contain several zip codes that do not 
necessarily have to be consecutive. It is important to clarify that each zone always has a value for each type of data
so that there will not be any blank space in our list, although if we can find values that are equal to 0, for example, 
there might be no men in some zone. The data is organized as follows:

1st Column: number of zip code, type integer (int). 
2nd Column: number of inhabitants, type integer (int). 
3rd Column: average age of the inhabitants, type integer (int). 
4th Column: number of male inhabitants, type integer (int). 
5th Column: number of female inhabitants, type integer (int). 
6th Column: number of households, type integer (int). 
7th Column: size of properties, float type data. 
8th Column: name of the neighborhood, string (str).
