<script lang="ts">
	import * as Sidebar from '$lib/components/ui/sidebar/index.js';
	import { ChartBar, FileText, Home, Settings, Users } from 'lucide-svelte';

	const items = [
		{
			title: 'Home',
			url: '/',
			icon: Home
		},
		{
			title: 'Projects',
			url: '/projects',
			icon: FileText
		},
		{
			title: 'Analytics',
			url: '/analytics',
			icon: ChartBar
		},
		{
			title: 'Team',
			url: '/team',
			icon: Users
		},
		{
			title: 'Settings',
			url: '/settings',
			icon: Settings
		}
	];
</script>

<Sidebar.Root collapsible="icon" class="z-50">
	<Sidebar.Header>
		<div class="flex h-[60px] items-center px-6">
			<span class="font-semibold">Risk Tool</span>
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
										<span>{item.title}</span>
									</a>
								{/snippet}
							</Sidebar.MenuButton>
						</Sidebar.MenuItem>
					{/each}
				</Sidebar.Menu>
			</Sidebar.GroupContent>
		</Sidebar.Group>
	</Sidebar.Content>
	<Sidebar.Footer>
		<div class="flex flex-col items-center justify-center px-6">
			<span class="text-muted-foreground text-sm">Generic FE v0.0.2</span>
			<div class="text-muted-foreground flex items-center gap-2 text-xs">
				<a
					href="https://sethvanwieringen.dev/"
					class="border-b border-transparent transition-all duration-200 hover:border-gray-400"
				>
					Seth van Wieringen
				</a>
				<span class="text-gray-400">•</span>
				<span>© {new Date().getFullYear()}</span>
			</div>
		</div>
	</Sidebar.Footer>
</Sidebar.Root>
