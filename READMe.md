# STRG

This program allows you to check the storage size of a file. Made this because I couldn't find something that already does this and I'm trying to make super super small programs, without the need to go out of visual studio code and use file explorer, and I couldn't be asked to actually google something for this.

## Usage

To use the program, follow the syntax below:

`python strg.py <file> [unit]`

The unit is optional. If not specified, it will display the size in all units.

## Example

`python strg.py strg.py`

`python strg.py strg.py B`

`python strg.py strg.py KB`

The supported units are:
<ul>
<li>B</li>
<li>KB</li>
<li>MB</li>
<li>GB</li>
<li>TB</li>
</ul>

## Example Output:

```
File size (B): 35823
File size (KB): 34
File size (MB): 0
File size (GB): 0
File size (TB): 0
```

## License

This program is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.