The Flex style uses less for its stylesheet. It turns out that if you don't
feel like installing npm for less, there's a Python package that you can
install using `pip install lesscpy` that does the job.

To convert the .less file to minified CSS, use the command

`lesscpy -X style.less ./style.min.css`