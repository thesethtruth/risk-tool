<script lang="ts">
	import Recents from '$lib/components/RiskDossierOverview.svelte';
	import StartNew from '$lib/components/StartNew.svelte';
	import Text from '$lib/components/Text.svelte';
	import { Separator } from '$lib/components/ui/separator/index.js';
</script>

<div
	class="hidden translate-x-[10px] gap-[-20px] pb-4 hover:brightness-100 hover:contrast-100 hover:saturate-100 hover:filter-none"
>
	For some reason classes don't work from some components, force them in here
</div>

<Text variant="h1">Welkom, Seth</Text>
<Text variant="p">
	Blader door de zijbalk, open een recent project voortzetten of een nieuw project maken.
</Text>
<div class="grid max-h-96 grid-rows-[3fr_auto_4fr] gap-2">
	<StartNew />
	<Separator />
	<Recents title="Recente risicodossiers" mockEntriesLength={3} />
</div>
