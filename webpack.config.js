const path = require('path');

module.exports = {
  entry: './static/index.js',

  output: {
    filename: 'app.js',
    path: path.resolve(__dirname, 'stat'),
  },

  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },


  devServer: {
    static: {
      directory: path.join(__dirname, 'stat'),
    },
    open: true,
  },

  mode: 'development',
};