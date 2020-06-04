module.exports = {
    "env": {
        "node": true,
        "browser": true,
        "es6": true
    },
    "parser": "babel-eslint",
    "extends": [
        "eslint:recommended",
        "plugin:react/recommended",
        "plugin:prettier/recommended",
        'plugin:import/errors',
        'plugin:import/warnings',
    ],
    "settings": {
        "react": {
            "version": "detect"
        }
    },
    "parserOptions": {
        "ecmaFeatures": {
            "jsx": true
        },
        "ecmaVersion": 2018,
        "sourceType": "module"
    },
    "plugins": ["react", "unused-imports"],
    "rules": {
        'consistent-return': 'warn',
        'import/no-unresolved': 'off',
        'import/order': 'warn',
        "no-unused-vars": "warn",
        "react/react-in-jsx-scope": "off",
        "react/jsx-filename-extension": "off",
        "react/display-name": "off",
        'react/prop-types': 'off',
        'sort-imports': ["warn", {
            "ignoreCase": false,
            "ignoreDeclarationSort": true,
            "ignoreMemberSort": false,
            "memberSyntaxSortOrder": ["none", "all", "multiple", "single"]
        }],
        "unused-imports/no-unused-imports": 'error',
        "unused-imports/no-unused-vars": 'warn',
    }
}