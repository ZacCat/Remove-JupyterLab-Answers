# Remove-JupyterLab-Answers

I put together a small python script that removes answer cells. Answer cells are identified differently for markdown and code cells, but spacing and capitalization will not affect either type.

+ __Markdown cells:__ An answer cell has the first line in the form of a header saying answer with a number following, e.g. "# Answer 3". It can be any level of header so something like "### Answer 3" would also work if a level 3 header fits your layout better. 

+ __Code cells:__ An answer cell is simply one with a comment on the top that says "# answer cell". Once again the number of #s doesn't matter. 

To use the script simply write the following in a command line:

    python3 remove-answers.py <input_file> <output_file>

__Note:__ this will overwrite the previous output file, if there is one.
