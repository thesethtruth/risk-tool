<script lang="ts">
	import Footer from '$lib/components/Footer.svelte';
	import Header from '$lib/components/Header.svelte';
	import AppSidebar from '$lib/components/app-sidebar.svelte';
	import * as Sidebar from '$lib/components/ui/sidebar/index.js';
	import '../app.css';
	let { children } = $props();
</script>

<div class="flex min-h-screen flex-col">
	<div class="grid flex-grow grid-cols-1 grid-rows-[auto_1fr_auto]">
		<Header />

		<Sidebar.Provider>
			<div class="z-50 flex">
				<AppSidebar />
				<main class="flex-1 p-6">
					<!-- Render children in the content area -->
					{@render children()}
				</main>
			</div>
		</Sidebar.Provider>

		<Footer />
	</div>
</div>
