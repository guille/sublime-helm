# Helm support for Sublime Text

Very personal use case, which is why I won't publish on Package Control. Most people are better off using [YamlPipelines](https://github.com/SublimeText/YamlPipelines/)

This package includes:
1. Syntaxes
	1. A custom YAML syntax with an extension to allow embedded json, helm or yaml inside the yaml
	2. A Helm syntax (inherits from the default Go template + the custom YAML with embeds)
	3. A HelmValues syntax to be applied to values.yaml. This is useful because [helm-ls](https://github.com/mrjosh/helm-ls) supports values.yaml but not normal yamls. So the Sublime Text solution is to have a custom scope for this case and restrict the language server to only start there. See [my dotfiles](https://github.com/guille/dotfiles/tree/master/sublime) for examples.
2. Language preferences for Helm (comments, etc), mirroring YAML
3. A build system that runs `helm package`

Not provided:
- Automatic assignment of syntaxes
