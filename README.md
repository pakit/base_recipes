# Recipes

[![Travis](https://travis-ci.org/pakit/base_recipes.svg?branch=master)](https://travis-ci.org/pakit/base_recipes)

This is the home of the base recipes for Pakit.

These recipes should work on Linux primarily, may make other
repositories to contain OS specific overrides.

If you want to contribute a recipe, please ensure it works before making a PR.
Try to reduce dependencies on other recipes to a minimum.

## Testing

A `Vagrantfile` is in the root of the project. Read it for details.
To quickly get testing:

```sh
vagrant box add boxcutter/ubuntu1510
vagrant up
vagrant ssh
```

When done, you can remove all traces with:
```sh
vagrant destroy -f
vagrant box remove boxcutter/ubuntu1510 --all
```
