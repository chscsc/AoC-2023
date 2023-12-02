<!-- TODO: Upload a transparent icon & use that instead -->
# <img src="https://avatars.githubusercontent.com/u/152345110" width="20"/>&nbsp;&nbsp;AoC-2023
Advent of code repository for the Century Computer Science Club.

## Branches
You may have noticed that there is no code in the `master` branch. All solutions are grouped by language in different branches.

| Language | Branch Name | Solved Days | Details | Contributor |
| -------- | ----------- | ----------- | ------- | ----------- |
| Python 3 | [`python`](https://github.com/chscsc/AoC-2023/tree/python)    | 1        | | Finn B |
| Java (17) | [`java`](https://github.com/chscsc/AoC-2023/tree/java)        | 1        | | Michael M |
| NodeJS | [`NodeJS`](https://github.com/chscsc/AoC-2023/tree/nodejs) | 1 | | Michael M |
| ReactJS | [`ReactJS`](https://github.com/chscsc/AoC-2023/tree/reactjs) | 1 | A web application. Modular enough that if you understand JavaScript you should be able to add days to it. | Michael M |
| C# | [`csharp`](https://github.com/chscsc/AoC-2023/tree/csharp) | 1 | | Finn B |
| C++ | [`cplusplus`](https://github.com/chscsc/AoC-2023/tree/csharp) | 1 | | Finn B |
| Rust | [`rust`](https://github.com/chscsc/AoC-2023/tree/rust) | 1 | | Finn B |
| C    | [`c`](https://github.com/chscsc/AoC-2023/tree/c) | 1.1 | There are a lot of bad practices going on here. | Michael M |

### Creating a new branch
If you (being a chscsc member) want to contribute code to this repository, then you need to create a branch.

1. Contribute your code
Please create a new branch, typically with the name of the language you are using. If a branch already exists with that name, add a number to the end. Put your contributions in this new branch.  
Also, please make an 'initial commit' in your branch that removes this branches section from the README. This prevents people from being confused when later language branches don't show up in the tables of older ones. An example commit that does this can be found [here for python](https://github.com/chscsc/AoC-2023/commit/5122b218c65959717403cf8fbb8965ed5d3f573c).
2. Create a pull request that adds your new branch to the table containing all branches. **OR** Have someone from the club leadership add it without a pull request by manually editing the README on [`github.com`](https://github.com/chscsc/AoC-2023/edit/master/README.md). This is the ideal method.

### Using a `.gitignore`
Please use a `.gitignore` file in every branch for the right language. [This page](https://www.freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo/) explains what a `.gitignore` file is, and how to write one. 

The `master` branch includes a `.gitignore` for C++ to remind people to replace it with one for their own language. 

If you don't want to spend the time to write a custom one, you can easily use [gitignore.io](https://www.toptal.com/developers/gitignore/) to generate one for your specific language/branch.

### Language Ideas
If you want to contribute a new language branch, but can't think of any ideas, here are a few to try out. Make sure to solve at least one AoC problem before contributing code.
* Java
* C#
* NodeJS
* C++
* Some kind of assembly
* [Piet](https://esolangs.org/wiki/Piet) 
* Choose a [random esolang](https://esolangs.org/wiki/Special:Random) from esolangs.org
