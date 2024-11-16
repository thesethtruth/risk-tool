<script lang="ts">
	import * as Sidebar from '$lib/components/ui/sidebar/index.js';
	import {
		Blocks,
		ChartBar,
		FileSearch,
		FileText,
		Home,
		SquareDashedMousePointer
	} from 'lucide-svelte';

	const items = [
		{
			title: 'Home',
			url: '/',
			icon: Home
		},
		{
			title: 'Risicodossiers',
			url: '/risk-dossiers',
			icon: FileText
		},
		{
			title: 'Dashboard',
			url: '/dashboard',
			icon: ChartBar
		},
		{
			title: 'Zoeken',
			url: '/search',
			icon: FileSearch
		}
	];
</script>

<Sidebar.Root collapsible="icon" class="z-50">
	<Sidebar.Header>
		<div class="flex h-[60px] items-center gap-3 px-6">
			<Blocks />
			<span class="font-semibold" data-collapsed-hide>Risico Tool</span>
		</div>
	</Sidebar.Header>
	<Sidebar.Content>
		<Sidebar.Group>
			<Sidebar.GroupContent>
				<Sidebar.Menu>
					{#each items as item (item.title)}
						<Sidebar.MenuItem>
							<Sidebar.MenuButton>
								{#snippet child({ props })}
									<a href={item.url} {...props}>
										<svelte:component this={item.icon} />
										<span data-collapsed-hide>{item.title}</span>
									</a>
								{/snippet}
							</Sidebar.MenuButton>
						</Sidebar.MenuItem>
					{/each}
				</Sidebar.Menu>
			</Sidebar.GroupContent>
		</Sidebar.Group>
		<Sidebar.Separator />
		<Sidebar.Group>
			<Sidebar.GroupContent>
				<Sidebar.Menu>
					<Sidebar.MenuItem>
						<Sidebar.MenuButton>
							{#snippet child({ props })}
								<a href="demo-page" {...props}>
									<SquareDashedMousePointer />
									<span data-collapsed-hide>Tijdelijk!</span>
								</a>
							{/snippet}
						</Sidebar.MenuButton>
					</Sidebar.MenuItem>
				</Sidebar.Menu>
			</Sidebar.GroupContent>
		</Sidebar.Group>
	</Sidebar.Content>
	<Sidebar.Footer>
		<span data-collapsed-hide>
			<div class="flex flex-col items-center justify-center gap-3 px-6">
				<span class="text-muted-foreground text-sm">Generic FE v0.0.2</span>
				<div class="text-muted-foreground flex items-center gap-2 text-xs">
					<a
						target="_blank"
						href="https://sethvanwieringen.dev/"
						class="border-b border-transparent transition-all duration-200 hover:border-gray-400"
					>
						Seth van Wieringen
					</a>
					<span class="text-gray-400">•</span>
					<span>© {new Date().getFullYear()}</span>
				</div>
			</div>
		</span>
	</Sidebar.Footer>
</Sidebar.Root>

<style>
	[data-collapsed-hide] {
		opacity: 1;
		transition: opacity 0.2s ease;
	}

	:global([data-state='collapsed']) [data-collapsed-hide] {
		opacity: 0;
		pointer-events: none;
	}
</style>
