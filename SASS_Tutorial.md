#SYNTACTICALLY AWESOME STYLE SHEETS

### Preprocessing
- **Install:** ```$ npm install -g sass```
- **Convert ```scss``` to ```css```:** ```$ sass stylesheet.scss style.css```
  - *converts .scss to .css (can rename in the process)*
- **Auto-convert ```scss``` to ```css```:** ```$ sass --watch input.scss output.css```
  - *Watch/output to folders:** ```$ sass --watch app/sass:static/stylesheets```
    - *rather than manually re-compiling the CSS file with every ```.scss``` change, the watch flag tells Sass to watch the source file for changes, and re-compile CSS each time you save your Sass. Watching folders will watch all files in the input source, and compile all CSS in the output folder.*

### Variables


<table>
  <tr>
    <th>SCSS</th>
    <th>CSS</th>
  </tr>
  <tr>
    <td>
    ```css
    $font-stack: Helvetia, sans-serif
    $primary-color: #333
    body {
      font: 100% $font-stack;
      color: $primary-color:
     }
    ```
    </td>
    <td>
    
    </td>
  <tr>
</table>
