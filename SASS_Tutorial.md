# SYNTACTICALLY AWESOME STYLE SHEETS
- [Sass](https://sass-lang.com/)

### Preprocessing
- **Install:** ```$ npm install -g sass```
- **Convert ```scss``` to ```css```:** ```$ sass stylesheet.scss style.css```
  - *converts .scss to .css (can rename in the process)*
- **Auto-convert ```scss``` to ```css```:** ```$ sass --watch input.scss output.css```
  - *Watch/output to folders:** ```$ sass --watch app/sass:static/stylesheets```
    - *rather than manually re-compiling the CSS file with every ```.scss``` change, the watch flag tells Sass to watch the source file for changes, and re-compile CSS each time you save your Sass. Watching folders will watch all files in the input source, and compile all CSS in the output folder.*

### Variables
- Sass allows the use of variables, entities you want to use again & again throughout the stylesheet: colors, font-stacks, &c. This is helpful when creating the stylesheet, so you don't have to copy & paste the website's primary color a dozen times, but also when modifying the stylesheet– you only have to make a change once, the variable value itself. Variables are prepended with ```$```. When Sass is processed, it replaces all ```$variable```s with the actual value.

<table>
<tr>
<th>SCSS</th>
<th>CSS</th>
</tr>
<tr>
<td>

```sass
/*VARIABLES*/
$font-stack:    Helvetica, sans-serif
$primary-color: #333

body
  font: 100% $font-stack
  color: $primary-color
```

</td>
<td>

```css
body {
  font: 100% Helvetica, sans-serif;
  color: #333;
}
```

</td>
</tr>
</table>



### Nesting
- HTML has a clear nested hierarchy, –CSS does not. Sass lets you nest CSS selectors just like HMTL (however, it's bad practice to overdo it).



<table>
<tr>
<th>SCSS</th>
<th>CSS</th>
</tr>
<tr>
<td>

```sass
nav
  ul
    margin: 0
    padding: 0
    list-style: none

  li
    display: inline-block

  a
    display: block
    padding: 6px 12px
    text-decoration: none
```

</td>
<td>

```css
nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
nav li {
  display: inline-block;
}
nav a {
  display: block;
  padding: 6px 12px;
  text-decoration: none;
}
```

</td>
</tr>
</table>


















