
%fprintf('sadnessXdificuldade: %f',corr(mediaQ.sadness, mediaQ.dificuldade));
%fprintf('sadnessXacertos: %f',corr(mediaQ.sadness, mediaQ.acertos));
%fprintf('sadnessXtempo: %f',corr(mediaQ.sadness, mediaQ.tempo));
%fprintf('sadnessXdiaMomento: %f',corr(mediaQ.sadness, mediaQ.diaMomento));
%fprintf('sadnessXsentindoAgora: %f',corr(mediaQ.sadness, mediaQ.sentindoAgora));
%fprintf('sadnessXhorasDeSono: %f',corr(mediaQ.sadness, mediaQ.horasDeSono));
%fprintf('sadnessXexpectativaVest: %f',corr(mediaQ.sadness, mediaQ.expectativaVestibular));
%fprintf('sadnessXdesempenhoEscola: %f',corr(mediaQ.sadness, mediaQ.desempenhoEscola));
%fprintf('sadnessXpreparacaoVest: %f',corr(mediaQ.sadness, mediaQ.preparacaoVestibular));
%fprintf('sadnessXcursinho: %f',corr(mediaQ.sadness, mediaQ.cursinho));
%fprintf('sadnessXMaisAfinidade: %f',corr(mediaQ.sadness, mediaQ.maisAfinidadeArea));
%fprintf('sadnessXMenosAfinidade: %f',corr(mediaQ.sadness, mediaQ.menosAfinidadeArea));
%fprintf('sadnessXSexo: %f',corr(mediaQ.sadness, mediaQ.sexo));
%fprintf('sadnessXAprovado: %f',corr(mediaQ.sadness, mediaQ.aprovado));
pearson = 1;
if pearson == 1
    disp('dificuldade Pearson');
    fprintf('%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n',corr(mediaQ.sadness, mediaQ.dificuldade),corr(mediaQ.neutral, mediaQ.dificuldade),corr(mediaQ.contempt, mediaQ.dificuldade),corr(mediaQ.disgust, mediaQ.dificuldade), corr(mediaQ.anger, mediaQ.dificuldade), corr(mediaQ.surprise, mediaQ.dificuldade), corr(mediaQ.fear, mediaQ.dificuldade), corr(mediaQ.happiness, mediaQ.dificuldade));
    disp('acertos');
    fprintf('%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n',corr(mediaQ.sadness, mediaQ.acertos),corr(mediaQ.neutral, mediaQ.acertos),corr(mediaQ.contempt, mediaQ.acertos),corr(mediaQ.disgust, mediaQ.acertos), corr(mediaQ.anger, mediaQ.acertos), corr(mediaQ.surprise, mediaQ.acertos), corr(mediaQ.fear, mediaQ.acertos), corr(mediaQ.happiness, mediaQ.acertos));

else
    disp('dificuldade Spearman');
    fprintf('%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n',corr(mediaQ.sadness, mediaQ.dificuldade,'Type','Spearman'),corr(mediaQ.neutral, mediaQ.dificuldade,'Type','Spearman'),corr(mediaQ.contempt, mediaQ.dificuldade,'Type','Spearman'),corr(mediaQ.disgust, mediaQ.dificuldade,'Type','Spearman'), corr(mediaQ.anger, mediaQ.dificuldade,'Type','Spearman'), corr(mediaQ.surprise, mediaQ.dificuldade,'Type','Spearman'), corr(mediaQ.fear, mediaQ.dificuldade,'Type','Spearman'), corr(mediaQ.happiness, mediaQ.dificuldade,'Type','Spearman'));
    disp('acertos');
    fprintf('%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n',corr(mediaQ.sadness, mediaQ.acertos,'Type','Spearman'),corr(mediaQ.neutral, mediaQ.acertos,'Type','Spearman'),corr(mediaQ.contempt, mediaQ.acertos,'Type','Spearman'),corr(mediaQ.disgust, mediaQ.acertos,'Type','Spearman'), corr(mediaQ.anger, mediaQ.acertos,'Type','Spearman'), corr(mediaQ.surprise, mediaQ.acertos,'Type','Spearman'), corr(mediaQ.fear, mediaQ.acertos,'Type','Spearman'), corr(mediaQ.happiness, mediaQ.acertos,'Type','Spearman'));
end