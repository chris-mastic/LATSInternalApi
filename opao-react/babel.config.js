module.exports = function (api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'],
    plugins: [
      'react-native-classname-to-style',
      ['react-native-platform-specific-extensions', { extensions: ['css'] }],
      [
        'module-resolver',
      {
        
        alias:{
          '@Src': "./src",
          '@Tests':  './tests',
          '@Screens': './src/pages',
          '@Components':'./src/components',
          '@Assets':'./assets',
                           
        }

      },
    ]
    ],
  };
};