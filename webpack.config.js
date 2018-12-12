var path = require('path')

module.exports = {
    devtool: 'source-map',
    entry: [
        './web_client/index.js'
    ],
    output: {
        path: `${__dirname}/xws/static`,
        filename: 'bundle.js',
        publicPath: '/static/'
    },
    devServer: {
        proxy: [{
            path: '/api/',
            target: 'http://localhost:3001'
        }],
        historyApiFallback: true
    },
    module: {
        loaders: [
            {
                test: /\.jsx?/,
                loaders: ['babel-loader'],
                include: path.join(__dirname, 'web_client')
            },
            {
                test: /\.css/,
                loaders: ['style-loader', 'css-loader'],
            }
        ]
    }
}