const CopyPlugin = require("copy-webpack-plugin");
const HtmlMinimizerPlugin = require("html-minimizer-webpack-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
const TerserPlugin = require("terser-webpack-plugin");
const glob = require("glob");

const entry = glob.sync("src/**/*.js")
    .reduce((x,y) => Object.assign(x, {
        [y.replace(/^src\//, '').replace('.js', '')]:'./'+y,
    }), {});

console.log(entry)

module.exports = {
    mode: "development",
    // entry: {
    //     home: './src/home.js',
    //     about: './src/about.js'
    //     // mp_inde
    // },
    plugins: [
        new CopyPlugin({
            patterns: [
                {
                    from: 'public',
                    to: './'
                }
            ]
        })
    ],
    entry,
    optimization: {
        minimize: true,
        minimizer: [
            new HtmlMinimizerPlugin(),
            new CssMinimizerPlugin(),
            new TerserPlugin(),
        ]
    }, 
    output: {
        path: __dirname+'/dist', 
        filename: "[name].bundle.js"
    }
}