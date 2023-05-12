const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");


module.exports = {
  entry: './static/index.js',

  output: {
    filename: 'app.js',
    path: path.resolve(__dirname, 'static/dict'),
  },

  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [MiniCssExtractPlugin.loader,
            "css-loader",
            "sass-loader",],
      }
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "app.css",
    }),
  ],


  devServer: {
    static: {
      directory: path.join(__dirname, 'static/dict'),
    },
    open: true,
  },

  mode: 'development',
};