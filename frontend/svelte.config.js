import adapter from '@sveltejs/adapter-node';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import { mdsvex } from 'mdsvex';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations
	// for more information about preprocessors
	preprocess: [vitePreprocess(), mdsvex()],

	kit: {
		// Use node adapter for production build
		adapter: adapter({
			// Node adapter options
			out: 'build'
		}),
		alias: {
			$lib: './src/lib'
		}
	},

	extensions: ['.svelte', '.svx']
};

export default config;
