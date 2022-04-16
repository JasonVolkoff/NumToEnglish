const path = require("path");

module.exports = {
    transpileDependencies: true,
    publicPath: "/static/src/vue/dist/",
    outputDir: path.resolve(__dirname, "../static/src/vue/dist/"),
    filenameHashing: false,
    runtimeCompiler: true,
    devServer: {
        proxy: {
            "^/api/": {
                target: "http://127.0.0.1:8000/api/",
            },
        },
        devMiddleware: { writeToDisk: true },
    },
};
