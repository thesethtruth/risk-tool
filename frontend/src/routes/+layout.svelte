<script lang="ts">
	import Footer from '$lib/components/Footer.svelte';
	import Header from '$lib/components/Header.svelte';
	import AppSidebar from '$lib/components/app-sidebar.svelte';
	import * as Sidebar from '$lib/components/ui/sidebar/index.js';
	import '../app.css';
	let { children } = $props();
</script>

<div class="flex flex-col">
	<Header />
	<div class="flex-1 overflow-auto">
		<Sidebar.Provider>
			<div class="flex">
				<AppSidebar />
				<div class="z-20 p-10">
					<!-- Render children in the content area -->
					{@render children()}
				</div>
			</div>
		</Sidebar.Provider>
	</div>
	<!-- <Footer /> -->
</div>
