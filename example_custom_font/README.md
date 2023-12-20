# Adding font

To use a font, simply install it on the operating system and use it in your report. If that doesn't work, you have the option to add a .jar file with the fonts you want to use along with the library. I've shown below how to do it.


## Step 1 - Understanding the structure

In the project repository, there's a folder with the base structure to perform the procedure. After cloning the repository, inside the folder where you cloned it, navigate to the **example_custom_font** directory

```
..
+-- example_custom_font
|	+-- src
|		+-- fonts
|			+-- myfontcustom
|				+-- CaskaydiaCoveNerdFont-Bold.ttf
|				+-- CaskaydiaCoveNerdFont-BoldItalic.ttf
|				+-- CaskaydiaCoveNerdFont-Italic.ttf
|				+-- CaskaydiaCoveNerdFont-Regular.ttf
|			+-- fontsfamily1703017000639.xml
|		+-- jasperreports_extension.properties
```

## Step 2 - Changes
1) Within the **fonts** folder, change the name of the folder `myfontcustom` to the name you want to use for the font in the report.

2) Copy the `.ttf` font files to the folder from the previous step. Specifically, the font files for `Regular`, `Bold`, `BoldItalic`, and `Italic`. Modify the corresponding file names within the `fontsfamily1703017000639.xml` file in their respective tags.

3) Using your preferred editor, open the file `fontsfamily1703017000639.xml`. Replace wherever you find the name `myfontcustom` with the same name you gave in step 1 of this section.


## Step 3 - Generating `.jar` file.

Compress the `fonts` folder along with the file `jasperreports_extension.properties`. Then, change the extension from `.zip` to `.jar` and name the `.jar` file with the same name as in `step 1` of the previous section, `Step 2 - Changes`.

## Step 4 - Using the generated `.jar` with the library.

Save the generated `.jar` in a folder of your choice, and in the `resource` parameter of the library, specify the folder where the `.jar` is located. Assign the font name in the report (`.jrxml`) and make good use of it.

## Reference

For further details, visit: [https://jasperreports.sourceforge.net/sample.reference/fonts/#fonts](https://jasperreports.sourceforge.net/sample.reference/fonts/#fonts)