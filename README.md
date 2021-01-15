# Initial-structure-project

Take and fuck

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install project.



```bash
pip install -r requirements/base.txt (linux)

pip install -r requirements\base.txt (windows)
```

## Folder front



use [prepros](https://prepros.io/downloads) to compile file scss

root directory for prepros ```'staticfiles'```

```

"projectName/staticfiles"


    css - 'dist folder'
        style.css - 'dist file style'
        reset.css - 'reset rules all browser and mobile browser'


    scss - 'source style folder'
        
        base - 
            _base.scss - 'global style' ### container settings is here
            _margin.scss - 'global margin'
            _mixin.scss - 'global mixin'
            _padding.scss - 'global padding'
            _typography.scss - 'global fonts'
            _vars.scss - 'global vars (color, background-color, box-shadow, border-radius)'

            ### create files scss with  "_" '_example.scss'


        components - 'create your components'
            _btn.scss - 'all button in site'
            _forms.scss - 'all forms in site'

             ### create component with  "_" '_example.scss'


        partials - 'this folder only _header.scss and _footer.scss'
            _btn.scss - 'all button in site'
            _forms.scss - 'all forms in site'

             ### create component with  "_" '_example.scss'
        

        pages
            _index.scss - 'create page style'

            ### _temp.scss - 'include files in the "pages folder" to the _temp.scss file'
        

        style.scss - 'includes all files scss and compile to css folder style.css'
```
