module.exports = {
    mode: "development",
    entry: {
        home: './src/home.js',
        about: './src/about.js'
    },
    output: {
        path: __dirname + '/dist', 
        filename: "[name].bundle.js"
    }
}