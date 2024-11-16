import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	optimizeDeps: {
		include: ['lucide-svelte']
	},
	resolve: {
		dedupe: ['svelte']
	}
});
