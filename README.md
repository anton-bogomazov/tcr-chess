# Chess Game

## Description
The project is a simple chess game engine.

BUT!

The main purpose of its implementation is to challenge the self in three different dimensions of dis-ease:
- Strict use of [Test && Commit || Revert](https://medium.com/@kentbeck_7670/test-commit-revert-870bbd756864)
- Python, which I'm still getting familiar with
- New to me JetBrains Fleet as a code editor

Important notes:
- Commits are not squashed intentionally

Todo:
- [x] Figures' moves logic
- [x] Game observer
- [x] Castling
- [x] Approval tests
- [x] Restrict jumping over figures
- [x] Game runner and GUI
- [x] More informative GUI
- [] <Rules> Implement en passant capturing

What I like about TCR:
- Although rolling back the changes was frustrating, it provided a sense of safety.
- It pushes you to test units of behaviour. When tests are to coupled with implementation,
change is impossible to made in a few TCR iterations because it is to big.
- Refactoring/Tidying is a great pleasure.
- It feels like playing in a hardcore game. I could compare it with Super Meat Boy (I am a huge fan) because of short cycles.

What I don't like:
- I made some bad design decisions because I couldn't see the big picture behind the small steps.
But, it was easy to refactor because of granularity of functions.
- Several times I've been overwhelmed by the complexity due to the inability to make changes small,
and the inability to do refactoring to make those changes easier to make.

I'm pretty sure it's not a flaw in TCR, but in my workflow on the project:
- A few times I got too caught up in a feature or design and neglected proper testing.
- I consciously started the project without analysis, wanting to test TCR as my only design tool.
Analyses are still needed (wow, how unexpected!)

Finally, mistakes I've made:
- Lack of analysis
- Abusing TCR by big steps
- Abusing TCR by copying chucks of code to clipboard

More about TCR [here](https://www.infoq.com/articles/test-commit-revert/)

Here are awesome workshops by Kent Beck:
- [Part 0](https://youtu.be/tnO2Mos0RjU?si=yj0RX3lT4aZ8RaSl)
- [Part 1](https://youtu.be/Aof0F9DvTFg?si=w4O3tstjAyZOsXcr)
- [Part 2](https://youtu.be/i3TUSxPy32A?si=WynMa-ySVXrMJK9e)
- [Part 3](https://youtu.be/9BBMj7OF4rc?si=6oi1hcALCPCCAImg)
- [Understanding Legacy Code with TCR](https://youtu.be/FFzHOyFeovE?si=yikGdcIcsBVA8mi9)