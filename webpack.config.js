var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,

  entry: './assets/js/index', // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs

  output: {
      path: path.resolve('./assets/bundles/'),
      filename: "[name]-[hash].js",
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],

  module: {
    rules: [
      { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader',
          query: {
              presets:['react'],
              plugins: [
                  ["import", {
                      libraryName: "antd",
                      style: true
                  }],
                  'transform-class-properties',
              ]
          }

      }, // to transform JSX into JS
      {
          test: /\.less$/,
          // use: ["style-loader", {loader: 'css-loader', options: {sourceMap: 1}}, "postcss-loader", "less-loader"]
          use: ["style-loader", {loader: 'css-loader', options: {sourceMap: 1}}, "less-loader"]
      }
    ],
  },

  resolve: {
    // modulesDirectories: ['node_modules', 'bower_components'],
    modules: ['node_modules'],
    // extensions: ['', '.js', '.jsx']
    extensions: ['.js', '.jsx']
  },
}
