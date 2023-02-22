import { sveltekit } from '@sveltejs/kit/vite';
import type { UserConfig } from 'vite';
import path from 'path';

const config: UserConfig = {
	plugins: [sveltekit()],

	resolve: {
		alias: {
			'$components': path.resolve('src/components'),
			'@': path.resolve('src/styles'),
		},
	},
};

export default config;
