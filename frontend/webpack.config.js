const HtmlWebPackPlugin = require("html-webpack-plugin")
const Dotenv = require('dotenv-webpack')

module.exports = {
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                use: { loader: "babel-loader" } 
            },
            {
                test: /\.html$/,
                use: { loader: "html-loader" }
            },
            {
                test: /\.(css|jpg|png)$/,
                use: { loader: "file-loader" }
            }
        ]
    },
    plugins: [
        new HtmlWebPackPlugin({
            template: "./public/index.html",
            filename: "./index.html"
        }),
        new Dotenv()
    ],
    devServer: {
        port: 8080,
        historyApiFallback: true
    }
}
