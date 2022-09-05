### How to start?
1. Install node and typescript.
2. Install ESLint extensions. (merged with TSLint already)
3. Install material icon theme as extension. 
4. Install path intellisense as extension for imports. 
5. Prettier - Code formatter (like black and isort in python). 
6. Create `index.html` via `html:5` in your file. And include the js file.
7. `tsc app.ts` to generate the javascript.
8. Run `npm init` and `npm install lite-server`. 
9. Add a line to package.json to start with lite-server. This should give real-time update.
10. Run `npm start`.

### How to use compiler+debugger? 
1. Run watch mode to tsc, only for one file. 
    ```
    tsc app.ts -w
    ```
2. Run the followings, 
    ```
    tsc --init
    tsc -w // for compiling all
    ```
3. Use sourceMap in tsconfig. This can help debugging in the browser to view ts scripts, and adding breakpoints.
4. Use outdir as `dist` so it stores all js files. 
5. Use rootdir with `src` so it will only scan `src`.
6. Run `npm start`. If you go to sources, you can introduce breakpoints to `src/*.ts`. 
