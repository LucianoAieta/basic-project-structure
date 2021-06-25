const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

module.exports = {
	mode: 'development',
	entry: {
		main: './src/ts/index.ts',
	},
	output: {
		path: path.resolve(__dirname + '/dist/'),
		filename: '[name].js',
	},
	module: {
		rules: [
			{
				test: /\.html$/,
				exclude: /node_modules/,
				use: 'html-loader',
			},
			{
				test: /\.(jpg|jpeg|png)$/,
				use: 'url-loader',
			},
			{
				test: /\.pug$/,
				use: ['pug-loader'],
			},
			{
				test: /\.sass$/i,
				use: ['style-loader', 'css-loader', 'sass-loader'],
			},
			{
				test: /\.ts?$/,
				use: 'ts-loader',
				exclude: /node_modules/,
			},
		],
	},
	resolve: {
		extensions: ['.ts', '.js'],
	},
	plugins: [],
};
