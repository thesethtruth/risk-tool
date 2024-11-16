<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import '../app.css';
	let { children } = $props();
</script>

<div class="flex min-h-screen flex-col">
	<div class="grid flex-grow grid-cols-1 grid-rows-[auto_1fr_auto]">
		<Header />

		<main class="grid flex-grow grid-cols-[30%_70%]">
			<nav class="bg-green-100">This is the content navigation pane.</nav>
			<div class="bg-red-100">
				<!-- Render children in the content area -->
				{@render children()}
			</div>
		</main>

		<footer class="bg-purple-100">This is the footer</footer>
	</div>
</div>
